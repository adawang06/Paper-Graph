#https://medium.com/@Jessicawlm/installing-neo4j-on-ubuntu-14-04-step-by-step-guide-#ed943ec16c56

#Security group:
#port 7687 for bolt
#22	tcp	12.131.20.202/32	✔
#7474	tcp	12.131.20.202/32	✔
#7473	tcp	12.131.20.202/32	✔
#7687	tcp	12.131.20.202/32	✔

#Neo4j version 3.1.4

#Get java8(java 10 is not compatible with Neo4j version 3.1.4)

$ java -showversion
$ sudo add-apt-repository ppa:webupd8team/java // we need to run this command for install java.
$ sudo apt-get update // using this command all dependency will be updated
$ sudo apt-get install oracle-java8-installer // now using this command java will be installed
$sudo apt-get update // using this command all dependency will be updated
$sudo apt install openjdk-8-jre-headless

After installing java now we will start the installation process for neo4j
$ wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
$ echo 'deb http://debian.neo4j.org/repo stable/' >/tmp/neo4j.list
$ sudo mv /tmp/neo4j.list /etc/apt/sources.list.d
$ sudo apt-get update // using this command all dependency will be updated

#Install neo4j 3.1.4 community edition
#$ sudo apt-get install neo4j=3.1.4

#Install neo4j 3.3.2 community edition
$ sudo apt-get install neo4j=3.3.2

#After completing installation process restart your neo4j service using below command.
$ sudo service neo4j restart

#To access neo4j using IP address please follow below process.
#First, open neo4j config file using below command.
$ sudo nano /etc/neo4j/neo4j.conf

#Now uncomment below line

#dbms.connector.http.address

#And put your IP address like below

#dbms.connector.http.listen_address = 10.0.0.11:7474(private IP address for AWS, not public IP address!)

#dbms.connector.bolt.listen_address = 0.0.0.0:7687

After completion, restart your neo4j service using below command

$sudo service neo4j restart

Access neo4j using public IPV4 address of AWS:

34.217.107.240:7474


