/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "usb.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <stdio.h>
#include <stdlib.h>
#include "string.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
int previousState = 0;
int currentState = 0;
int time_obs_us = 0.0;
float distance_cm = 0.0;
int startTimeECHO;
int endTimeECHO;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_I2C1_Init();
  MX_SPI1_Init();
  MX_USB_PCD_Init();
  MX_UART4_Init();
  MX_USART2_UART_Init();
  MX_TIM1_Init();
  /* USER CODE BEGIN 2 */

  uint8_t retours[] = "";

  int vitesseDroit = 30;
  int vitesseRotation = 10;

  /* Détection d'obstacles - Benoit */

  TIM1->CCR1 = 30;
  HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);

  //***********************************************************************************************
  float get_distance_obstacle()
  {
   int compteur = 0;
   while(compteur < 2){
	   currentState = HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_9);; //Lecture de l'état de ECHO
	      if ( currentState != previousState) {
	   	  if (currentState){
	   		  startTimeECHO = TIM1->CNT; // Enregistrement du temps de début de l'écho
	   		  compteur= 1;
	   	  }
	   	else{
	   	    endTimeECHO = TIM1->CNT; // Enregistrement du temps de fin de l'écho
	   	    compteur = 2;
	   		}

   }
   previousState = currentState;
  }
   //*******************************Calcul de la durée et distance****************************************
  time_obs_us = (endTimeECHO - startTimeECHO)*10; // Calcul de la durée de l'écho en micros secondes
  distance_cm = time_obs_us / 58; // Calcul de la distance en centimètres
  compteur = 0;
  return distance_cm;
  }

  void obstacles_detecte()
  {
	  uint8_t Stop[] = "stop\r";
	  uint8_t Arriere[] = "mogo 1:-10 2:-10\r";
	  uint8_t value = 'p';

	  distance_cm = get_distance_obstacle();

	  while (distance_cm <= 70.0) {
		  HAL_UART_Receive(&huart4, &value, strlen(value), 100);

		  if (value == 's') {
		  		HAL_UART_Transmit(&huart2, Arriere, strlen(Arriere),  HAL_MAX_DELAY);
		  }

		   HAL_UART_Transmit(&huart2, Stop, strlen(Stop),  HAL_MAX_DELAY);
		   distance_cm = get_distance_obstacle();
	  }
  }

  /* Suivi de lignes - Valentina */

  int capteur1()
  {
	  if(HAL_GPIO_ReadPin(Sensor1_GPIO_Port, Sensor1_Pin))
	  {
		  return 0; //Detect line
	  }
	  else
	  {
		  return 1; //Does not detect line
	  }
  }

  int capteur2()
  {
	  if(HAL_GPIO_ReadPin(Sensor2_GPIO_Port, Sensor2_Pin))
	  {
		  return 0; //Detect line
	  }
	  else
	  {
		  return 1; //Does not detect line
	  }
  }

  int follow_line(s1,s2)
  {

  uint8_t Avance[] = "digo 1 : 1000 : 20 2 : 1000 : 20\r";
  uint8_t Droite90[] = "digo 1 : -510 : 25 2 : 510 : 25\r";
  uint8_t Gauche90[] = "digo 1 : 510 : 25 2 : -510 : 25\r";

  uint8_t VelocityInfo[] = "vel\r";

   if(s1==1 && s2==1)
   {
	   HAL_UART_Transmit(&huart2, Avance, strlen(Avance),  HAL_MAX_DELAY);
	   HAL_Delay(100);
	   HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	   HAL_UART_Receive(&huart2, &retours, 20,  500);
	   HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);;
   }
   else if(s1==0 && s2==1)
   {
	    HAL_UART_Transmit(&huart2, Gauche90, strlen(Gauche90),  HAL_MAX_DELAY);
		HAL_Delay(100);
		HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
		HAL_UART_Receive(&huart2, &retours, 20,  500);
		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
   }
   else if(s1==1 && s2==0)
   {
	   HAL_UART_Transmit(&huart2, Droite90, strlen(Droite90),  HAL_MAX_DELAY);
	   HAL_Delay(100);
	   HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	   HAL_UART_Receive(&huart2, &retours, 20,  500);
	   HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
   }
   else
   {
	uint8_t value = 'p';
   }
  }

  /* Suivi de lignes - Valentina */


  /* Getter de retours de la vélocité des roues du robot */

  int get_velocity_roue_gauche(retours)
  {
	  char * separator;
	  int values[2];

	  // On divise la chaine de caractères retours en deux entiers
	  separator = strtok((char*)retours, " ");
	  values[0] = atoi(separator); // Convertir la première partie en entier
	  separator = strtok(NULL, " ");
	  values[1] = atoi(separator); // Convertir la deuxième partie en entier

	  return values[0];
  }

  int get_velocity_roue_droite(retours)
  {
	  char * separator;
	  int values[2];

	  // On divise la chaine de caractères retours en deux entiers
	  separator = strtok((char*)retours, " ");
	  values[0] = atoi(separator); // Convertir la première partie en entier
	  separator = strtok(NULL, " ");
	  values[1] = atoi(separator); // Convertir la deuxième partie en entier

	  return values[1];
  }

  void motors_functions(value, vitesseDroit, vitesseRotation)
  {

	  uint8_t Start[20];
	  uint8_t Gauche[20];
	  uint8_t Droite[20];
	  uint8_t Arriere[20];

	  sprintf(Start, "mogo 1:%d 2:%d\r", vitesseDroit, vitesseDroit);
	  sprintf(Gauche, "mogo 1:%d 2:-%d\r", vitesseRotation, vitesseRotation);
	  sprintf(Droite, "mogo 1:-%d 2:%d\r", vitesseRotation, vitesseRotation);
	  sprintf(Arriere, "mogo 1:-%d 2:-%d\r", vitesseDroit, vitesseDroit);


	  uint8_t Droite90[] = "digo 1 : -510 : 25 2 : 510 : 25\r";
	  uint8_t Gauche90[] = "digo 1 : 510 : 25 2 : -510 : 25\r";

	  uint8_t Stop[] = "stop\r";

	  uint8_t GaucheDrift[] = "mogo 1:50 2:-50\r";
	  uint8_t DroiteDrift[] = "mogo 1:-50 2:50\r";

	  uint8_t VelocityInfo[] = "vel\r";

	  switch(value)
	  	  {

	  	  case('z'):
	  		HAL_UART_Transmit(&huart2, Start, strlen(Start),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  	  	break;

	  	  case('s'):
	  		HAL_UART_Transmit(&huart2, Arriere, strlen(Arriere),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  	  	break;

	  	  case('d'):
	  	  	HAL_UART_Transmit(&huart2, Droite, strlen(Droite),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  	  	break;

	  	  case('q'):
	  	  	HAL_UART_Transmit(&huart2, Gauche, strlen(Gauche),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  	  	break;

	  	  case('p'):
	  	  	HAL_UART_Transmit(&huart2, Stop, strlen(Stop),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  		break;

	  	  case('G'):
	  		HAL_UART_Transmit(&huart2, Gauche90, strlen(Gauche90),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		HAL_Delay(2000);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  		break;

	  	  case('D'):
	  		HAL_UART_Transmit(&huart2, Droite90, strlen(Droite90),  HAL_MAX_DELAY);
	  	  	HAL_Delay(500);
	  	  	HAL_UART_Transmit(&huart2, VelocityInfo, strlen(VelocityInfo),  HAL_MAX_DELAY);
	  		HAL_UART_Receive(&huart2, &retours, 20,  500);
	  		HAL_UART_Transmit(&huart4, retours, strlen(retours), 500);
	  		HAL_Delay(2000);
	  		get_velocity_roue_gauche(retours);
	  		get_velocity_roue_droite(retours);
	  		break;
	  	  };
  };

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

	  /*FONCTIONS POUR LE CONTROLE DU ROBOT */

	  int s1;
	  int s2;

	  uint8_t value = 'p';
	  s1 = capteur1();
	  s2 = capteur2();

	  HAL_UART_Receive(&huart4, &value, strlen(value), 100);

	  HAL_Delay(100);

	  obstacles_detecte();

	  follow_line(s1, s2);

	  motors_functions(value, vitesseDroit, vitesseRotation);

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI|RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL6;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USB|RCC_PERIPHCLK_USART2
                              |RCC_PERIPHCLK_UART4|RCC_PERIPHCLK_I2C1
                              |RCC_PERIPHCLK_TIM1;
  PeriphClkInit.Usart2ClockSelection = RCC_USART2CLKSOURCE_PCLK1;
  PeriphClkInit.Uart4ClockSelection = RCC_UART4CLKSOURCE_PCLK1;
  PeriphClkInit.I2c1ClockSelection = RCC_I2C1CLKSOURCE_HSI;
  PeriphClkInit.USBClockSelection = RCC_USBCLKSOURCE_PLL;
  PeriphClkInit.Tim1ClockSelection = RCC_TIM1CLK_HCLK;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
