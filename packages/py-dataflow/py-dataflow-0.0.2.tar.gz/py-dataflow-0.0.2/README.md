# py-pack  

Generate package egg, that can be attached to Spark clusters in production or included in a PySpark console.

$ python=3.6.1

python setup.py bdist_wheel sdist
twine upload dist\*

### Install dependences
	pip install -r requirements.txt

### Create module pypack
	python setup.py install

### Test solutions 
	python tests/test_mission.py 

### Command line to Generate package egg, your code in a dist/pypack-0.0.1-py3.6.egg 
	python setup.py bdist_egg

### Start the PySpark console and attach the egg file.
	pyspark --py-files dist/pypack-0.0.1-py3.6.egg


### From the PySpark REPL, you can import the pypack code and execute the application code.

+ from pypack.spark import *
+ from pypack.mission import with_life_goal
+ source_data = [ ("jose", 1), ("pedro", 2) ]
+ source_df = spark.createDataFrame( source_data, ["name", "age"])
+ actual_df = with_life_goal(source_df)
+ actual_df.show()



### The pypack library can be attached to spark-submit commands for launching applications in a similar manner.



DATAFLOW
Processamento simplificado de dados de stream e em lote, com a mesma confiabilidade e expressividade
AVALIAÇÃO GRATUITA
Desenvolvimento mais rápido e gerenciamento mais simples
O Cloud Dataflow é um serviço totalmente gerenciado para transformar e aprimorar dados nos modos de stream (tempo real) e em lote (do histórico) com a mesma confiabilidade e expressividade. Você não precisa mais encontrar soluções alternativas complexas. E, com a abordagem sem servidor para o provisionamento e gerenciamento de recursos, você tem acesso a uma capacidade praticamente ilimitada para solucionar seus maiores desafios de processamento de dados, ao mesmo tempo em que paga apenas por aquilo que usa.

O Cloud Dataflow habilita casos de uso transformacionais em vários setores, incluindo:

check análise de sequência de cliques, pontos de venda e segmentação no varejo
check detecção de fraude em serviços financeiros
check experiência do usuário personalizada em jogos
check análises da IoT na indústria, em serviços de saúde e em logística
faster-development-easier-management
Desenvolvimento acelerado para dados em lote e de stream
O Cloud Dataflow possibilita o desenvolvimento rápido e simplificado de canais por meio das APIs expressivas de Java e Python no SDK do Apache Beam. Ele oferece um conjunto avançado de primitivos de análise de sessão e janelas, assim como um ecossistema de conectores de coletor e origem. Além disso, com o modelo de desenvolvimento exclusivo e unificado do Beam, é possível reutilizar mais códigos nos canais de stream e em lote.

accelerate-development-with-no-compromises
Simplifique operações e gerenciamento
A abordagem sem servidor do GCP remove a sobrecarga operacional com o processamento automático de desempenho, escalonabilidade, disponibilidade, segurança e conformidade. Desta forma, os usuários podem se concentrar na programação em vez de precisar gerenciar clusters de servidores. A integração com o Stackdriver, a solução de monitoramento e geração de registros unificada do GCP, permite que você faça o monitoramento e resolva problemas nos seus canais enquanto eles estão em execução. A visualização avançada, a geração de registros e o sistema de alertas avançado ajudam você a identificar e a tomar medidas em relação a possíveis problemas.

simplify-operations-and-management
Desenvolva a base para o machine learning
Use o Cloud Dataflow como um elemento de integração prático para incluir a análise preditiva na detecção de fraude, na personalização em tempo real e em casos de uso semelhantes. Para isso, adicione modelos do Cloud Machine Learning com base no TensorFlow e APIs nos seus canais de processamento de dados.

build-on-a-foundation-for-machine-learning
Use ferramentas que você conhece e prefere
O Cloud Dataflow se integra perfeitamente aos serviços do GCP para o processamento de eventos de streaming (Cloud Pub/Sub), armazenamento de dados (BigQuery), machine learning (Cloud Machine Learning) e muito mais. Com o SDK com base em Beam, os desenvolvedores também podem criar extensões personalizadas e até mesmo escolher mecanismos de execução alternativos, como o Apache Spark, por meio do Cloud Dataproc ou no local. Para os usuários do Apache Kafka, um conector do Cloud Dataflow facilita a integração com o GCP.

use-your-favorite-and-familiar-tools
Transformação de dados com o Cloud Dataflow
diagram-dataflow

RECURSOS DO CLOUD DATAFLOW
Gerenciamento de recursos automatizado
O Cloud Dataflow automatiza o provisionamento e o gerenciamento de recursos em processamento para reduzir a latência e maximizar a utilização. Você não precisa mais executar instâncias manualmente ou reservá-las.
Reequilíbrio dinâmico de trabalho
O particionamento automatizado e otimizado do trabalho reequilibra as atividades atrasadas de maneira dinâmica. Não é preciso procurar teclas de atalho ou fazer o pré-processamento dos seus dados de entrada.
Processamento único, confiável e consistente
Fornece suporte integrado para a execução tolerante a falhas consistente e correta, independentemente do tamanho dos dados, do tamanho do cluster, do padrão de processamento e da complexidade do canal.
Escalonamento automático horizontal
Escalonamento automático horizontal do número de workers para alcançar os melhores resultados de capacidade com o melhor custo-benefício.
Modelo de programação unificado
O SDK do Apache Beam oferece operações avançadas, similares ao MapReduce e de igual potência, além de sistema de gestão de janelas avançado e controle de correção detalhado tanto para os dados de stream quanto em lote.
Inovações voltadas para a comunidade
Os desenvolvedores que quiserem estender o modelo de programação do Cloud Dataflow podem fazer bifurcações e/ou contribuir para o Apache Beam.