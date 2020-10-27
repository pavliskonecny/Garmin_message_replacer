# Garmin_message_replacer v1.0 ENGLISH
Connect you Garmin device to PC/MAC and find language file at: Garmin/Text/Czech.gtt (or different language).
As first - MAKE BACKUP of this file to your PC/MAC.
Open this file and find word "CANNED".
You should get similar result:

<tag>TXT_CANNED_MESSAGE_List_10_Min_Away_STR_M</tag>
    <txt>Budu tam za 10 minut.</txt>

For each answer exists two records of "CANNED". So you should find this record also:

<tag> TXT_CANNED_MESSAGE_Prompt_10_Min_Away_STR_M </tag>
    <txt>Budu tam za 10 minut.</txt>

You can replace texts between markers <TXT> and </TXT> as you want.
But BE CAREFUL! The same text has to be two times for CANNED message (as you can see above).
After replacing, save file and copy the file to origin place in Garmin device.

It can be done by simple text editor. So what does application "Garmin message replacer" do?
In case Garmin release new update of your device, mostly update language file also. So your changes are lost...
By this program you can return your requested changes by few clicks.
In text editor open the configuration file "config.json" which is important part of this program.
Inside you can find tags <TAG> and corresponding texts <TXT>.
The configuration file "config.json" is like a template for replacing text messages.
So edit the file as you need.
In case that Garmin release update and make language file as default, simply run the application:
1. Open the language file *.gtt
2. Click on START button (it will start replacing texts according to template "config.json")
3. Save new (edited) language file
4. This new (edited) file you have to copy to origin place in Garmin device

DON'T FORGET to make a backup before replacing original file
Use of this program is on your own risk!
It was tested with device Garmin Edge530 and Windows 10.
Enjoy!

**********************************************************************************************************************************************

# Garmin_message_replacer v1.0 CZECH
Po pripojeni zarizeni pres USB k pocitaci, najdete jazykovy soubor v adresari: Garmin/Text/Czech.gtt (v pripade jineho jazyka zvolte vlastni).
Nejprve tento soubor nakopirujte nekam do PC/Mac jako zalohu.
Otevrete jazykovy soubor a vyhledejte slovo "CANNED".
Meli byste najit podobne vysledky jako tento:

<tag>TXT_CANNED_MESSAGE_List_10_Min_Away_STR_M</tag>
    <txt>Budu tam za 10 minut.</txt>

Pro kazdou odpoved vsak existuji 2 zaznamy  "CANNED". Nasledujici zaznam naleznete v souboru pozdeji:

<tag> TXT_CANNED_MESSAGE_Prompt_10_Min_Away_STR_M </tag>
    <txt>Budu tam za 10 minut.</txt>

Texty mezi znackami <TXT> a </TXT> muzete libovolne zmenit.
Ale POZOR! Stejny text dvakrat! (jako muzete videt vyse)
Po ulozeni takto upraveneho souboru, staci soubor nakopirovat zpet na puvodni misto v Garmin zarizeni.

Toto lze udelat v jakemkoliv textovem editoru. K cemu tedy slouzi program Garmin message replacer?
Pokud Garmin vyda update pro vase zarizeni, ve vetsine pripadu se prepise i jazykovy soubor a vase zmeny jsou pryc...
Tento program vam ale zmeny vrati na par kliknuti.
V textovem editoru otevrete soubor "config.json" ktery je nedilnou soucasti programu.
V nem naleznete tagy <TAG> a k nem patricne texty <TXT>.
Soubor "config.json" slouzi tedy jako sablona pro nahrazovani textovych zprav.
Upravte jej tedy jak potrebujete.
Pokud Garmin udela update, jednoduse spuste program:
1. Vyberte jazykovy soubor *.gtt
2. Stisknete tlacitko START a nahradite puvodni texty dle sablony "config.json"
3. Ulozte novy (upraveny) jazykovy soubor
4. Tento nove ulozeny soubor nahrajte na puvodni misto v zarizeni Garmin

NEZAPOMENTE PROVEST ZALOHU!
Pouziti je pouze na vasi vlastni zodpovednost!
Testovano na zarizeni Edge530 a Windows 10.
At se libi!