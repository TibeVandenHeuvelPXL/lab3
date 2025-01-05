## Part 1: Install the virtual lab environment
## Part 2: Install the CSR1000v VM
## Part 3: Python Network automation with NETMIKO
* Task Preparation and Implementation

Voordat ik aan deze taak begon heb ik de voorbeelden van de python scripts bekeken om een idee te krijgen hoe ik de taak zou oplossen. Ik heb stap voor stap iedere bulletpoint opgelost. Wanneer ik iets niet wist, heb ik dit opgezocht op het internet. Nadat ik iedere bulletpoint van taak 3 had opgelost, had ik een slordig script. Daarom heb ik daarna het script herschreven en gebruik gemaakt van meer functies en commenteer om het iets duidelijker te maken.
* Task Troubleshooting

Mijn 2de VM waarop de virtuele router stond werkte voordat ik aan deze opdracht begon nog, maar tijdens dat ik de opdracht was aan het maken deed deze het op de een of andere manier niet meer. Ik heb daarna gewoon deze 2de VM opnieuw geinstalleerd, en daarna heb ik de opdracht kunnen vervolledigen.
* Task Verification

Nadat ik ieder bulletpoint had opgelost, heb ik via show commandos of show run gekeken of hetgene effecties was toegepast. Maar in mijn script had ik eigenlijk ook al vaak commandos erbij gezet om aan te tonen dat het effecties werkt. In de map 'part3' op github heb ik zowel mijn script als mijn output toegevoegd als bewijs dat alle bulletpoints van taak 3 werken.
## Part 4: Explore YANG Models
## Part 5: Use NETCONF to Access an IOS XE Device
* Task Preparation and Implementation

Ik ben stap voor stap doorheen het lab gegaan. Hierbij heb ik gebruik gemaakt van Visual Studio Code en de terminal.
* Task Troubleshooting
* Task Verification

Aan de hand van de console messages en xml data die terug kwam kon je weten indien het script goed of fout was. Indien je geen foutmeldingen kreeg wist je dat er geen fouten in het script staan. Ook door show commandos op de router te doen wist je of de configuratie goed was doorgekomen. In de map 'part5' op github heb ik het script staan.
## Part 6: Use RESTCONF to Access an IOS XE Device
* Task Preparation and Implementation

Ik heb ook deze taak gewoon stap voor stap gevolgd. Ik heb gebruik gemaakt van Postman, Visual Studio Code en de terminal.
* Task Troubleshooting

In restconf-put.py script had ik een fout in de url waardoor ik een 404 error kreeg. Na een aantal keren het script te herlezen zag ik de fout in de url. Daarna kreeg ik de juiste code, namelijk een 201.
* Task Verification

Aan de hand van de codes die je terugkrijgt weet je direct als het juist of fout is. 200 codes betekent dat het goed is, 400 codes betekent dat het fout is. Ook heb ik op de router de 'show ip interface brief' commando gebruikt om te controleren als de loopback interface effecties was aangemaakt. Ik heb de scripts in de map 'part6' op github staan.
## Part 7: Getting started with NETCONF/YANG – Part 1
* Task Preparation and Implementation

Voor ik aan deze taak begon, heb ik de documentatie gelezen. Ik heb RPC calls gedaan, en informatie opgezocht op het internet wanneer ik iets niet snapte. Bij deze taak heb ik alleen de terminal gebruikt. Hieronder is een voorbeeld van een RPC call om de beschrijving van de G1 interface te veranderen.
1. Connectie met de virtuele router via NETCONF

```
ssh -s -p 830 username@host netconf
```
2. Reageren tegen de <hello> message

```
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
  </capabilities>
</hello>]]>]]>
```
3. edit-config RPC call

```
<?xml version="1.0" encoding="UTF-8"?>
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>1</name>
            <description>test</description>
          </GigabitEthernet>
        </interface>
      </native>
    </config>
  </edit-config>
</rpc>]]>]]>
```

* Task Troubleshooting

Eerst wijzigde de beschrijving van G1 niet omdat ik vergeten was te reageren op de <hello> message. Na opzoekingswerk kwam ik hier achter, en daarna lukte het me wel om de beschrijving van G1 te wijzigen.
* Task Verification

Deze taak kan ik aan de hand van 2 bewijzen tonen dat deze succesvol was. Ten eerste kreeg ik een response terug nadat ik de RPC call deed:
```
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101"><ok/></rpc-reply>]]>]]>
```
Daarnaast ben ik in de running config gaan kijken op de virtuele router, en hier was de beschrijving verandert:
![image](https://github.com/user-attachments/assets/4373bf98-1c9c-479b-9b46-92c08ba4ed8f)

## Part 8: Getting started with NETCONF/YANG – Part 2
* Task Preparation and Implementation
* Task Troubleshooting
* Task Verification
