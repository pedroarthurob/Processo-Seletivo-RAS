void setup()
{
  pinMode(13, OUTPUT);
}

void loop()
{
  int myDelay = 2000;
  
  // Loop para diminuir gradualmente o atraso
  for(int i = 1; i <= 20; i++)
  {
     
    digitalWrite(13, HIGH);//Liga o LED no pino 13
    delay(myDelay);//Aguarda o myDelay em milisegundos
    digitalWrite(13, LOW);//Desliga o LED no pino 13
    delay(myDelay);//Aguarda o myDelay em milisegundos
    myDelay *= 0.8; // Diminuindo o atraso em 20% a cada iteração
  }
  
  while(true)
  {
    digitalWrite(13, HIGH);
    delay(myDelay); // Mantém a última frequência definida
    digitalWrite(13, LOW);
    delay(myDelay);
  }
}