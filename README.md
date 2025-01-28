# Fundamentos de Linguagem Python Para Analise de Dados e Data Science
Repositório destinado aos projetos realizados durante a formação "Fundamentos de Linguagem Python Para Análise de Dados e Data Science" da plataforma Data Science Academy (DSA). A formação foi dividida em três níveis: Introdutório, Básico e Intermediário; cada um contendo seus projetos e desafios para reforçarem o conteúdo.

---

## Nível Introdutório

Seguindo o pseudocódigo para da execução do jogo da forca:
  1. INÍCIO
  2. Definir a palavra secreta (palavra_secreta)
  3. Definir a quantidade máxima de tentativas (tentativas_max)
  4. Criar uma lista para armazenar as letras corretas (letras_corretas)
  5. Criar uma lista para armazenar as letras erradas (letras_erradas)
  6. Definir o número de tentativas restantes (tentativas_restantes = tentativas_max)
  
  7. ENQUANTO tentativas_restantes > 0 FAÇA:
      1. Exibir o estado atual da palavra (com traços para letras não adivinhadas)
      2. Exibir as letras erradas já tentadas
      3. Solicitar ao jogador que insira uma letra (letra)
  
      4. SE letra ESTÁ em palavra_secreta ENTÃO:
          1. Adicionar letra à lista letras_corretas
          2. SE todas as letras de palavra_secreta ESTÃO em letras_corretas ENTÃO:
              1. Exibir mensagem de vitória ("Você venceu!")
              2. FIM
      5. SENÃO:
          1. Adicionar letra à lista letras_erradas
          2. Reduzir tentativas_restantes em 1
          3. Exibir mensagem de erro ("Letra incorreta!")
  
  8. FIM DO ENQUANTO
  
  9. SE tentativas_restantes == 0 ENTÃO:
      1. Exibir mensagem de derrota ("Você perdeu! A palavra era: palavra_secreta")
  10. FIM

- Primeira versão
  ![image](https://github.com/user-attachments/assets/2d366bd0-9292-4c85-b368-9a8f5d153759)

- Segunda versão
  ![image](https://github.com/user-attachments/assets/bda1e70e-100b-4e65-b110-a3d98697f1f8)

Enquanto a primeira versão se concentrou apenas em realizar a identificação da palavra e a contabilização do número de tentativas, na segunda versão foram implementados identificadores de repetição de letras, a representação da forca e a possibilidade de iniciar um novo jogo.
