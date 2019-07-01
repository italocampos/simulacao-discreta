# Trabalho extra da disciplina de Simulação Discreta
##### Professor: Filipe Saraiva
##### Monitoria: Italo Campos

Um aeroporto opera com voos de pequeno e grande porte, os quais são executados em pistas separadamente apropriadas. Aviões de pequeno porte pousam e decolam em pistas pequenas e aviões de grande porte, por sua vez, pousam e decolam em pistas grandes. Após a chegada de um avião, o mesmo é direcionado da pista de pouso para uma plataforma de descarga e desembarque, que esteja disponível, seguindo obrigatoriamente, após esse processo, para um hangar, onde serão realizados os preparativos para a próxima viagem. Cada hangar tem a capacidade para comportar uma aeronave por vez.

Ao estar preparada, uma aeronave desloca-se para as área de carga e embarque e aguarda por uma plataforma disponível, onde será realizado o embarque de passageiros e/ou cargas. Após esse procedimento, a aeronave dirige-se para uma pista disponível, onde realizará os procedimentos de decolagem. 

Para modelar este problema, considere que:

+ após o processo de pouso ou decolagem, uma pista fica imediatamente disponível;
+ o aeroporto dispõe de:
    - 5 plataformas de embarque/desembarque;
    - 3 hangares de reparos;
    - 2 pistas para aeronaves de pequeno porte;
    - 1 pista para aeronaves de grande porte;
    - fixe os tempos das atividades internas do aeroporto em:
        - pouso e decolagem de aeronaves de pequeno porte: 10 minutos;
        - pouso e decolagem de aeronaves de grande porte: 20 minutos;
        - desembarque de aeronaves de pequeno porte: 15 minutos;
        - desembarque de aeronaves de grande porte: 30 minutos;
        - embarque de aeronaves de pequeno porte: 30 minutos;
        - embarque de aeronaves de grande porte: 45 minutos;
+ despreze o tempo de locomoção das aeronaves nas dependências do aeroporto.