# def class MbtiPersonalityTest():
#     private final static Scanner input = new Scanner(System.in);
#     private static String[] arrayEI = new String[6];
#     private static String[] arraySN = new String[5];
#
#     private static String[] arrayTF = new String[5];
#
#     private static String[] arrayJP = new String[5];
#
#     private static int counterEIA;
#     private static int counterEIB;
#     private static int counterSNA;
#     private static int counterSNB;
#     private static int counterTFA;
#     private  static int counterTFB;
#     private static int counterJPA;
#     private static int counterJPB;
#     private static String realPersonality = "";
#
#     public static void main(String[] args) {
#         test1();
#         test2();
#         test3();
#         test4();
#         test5();
#         test6();
#         test7();
#         test8();
#         test9();
#         test10();
#         test11();
#         test12();
#         test13();
#         test14();
#         test15();
#         test16();
#         test17();
#         test18();
#         test19();
#         test20();
#         displayResult();
#
#     }
#
#     public static void test1() {
#         System.out.println("What is your name ");
#         String name  = input.next();
#         if (name.matches("^[a-zA-Z]+$")) {
#         }
#         else {
#             System.out.println("Invalid input");
#             test1();
#         }
#         System.out.println("A. Expend energy, enjoy groups \t\t\t B. Conserve energy, one-on-one");
#         arrayEI[0] = "Hello " + name +"\tyou selected : ";
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayEI[1] = "A. Expend energy, enjoy groups.";
#             counterEIA++;
#         } else if (option.equalsIgnoreCase("B")){
#             arrayEI[1] = "B. Conserve energy, one-on-one";
#             counterEIB++;
#         }
#         else{
#             System.out.println("Select A or B");
#             test1();
#         }
#     }
#
#     public static void test2() {
#         System.out.println("A. Interpret literally\t\t\t B. Look for meaning and possibilities");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")) {
#             arraySN[0] = "A. Interpret literally";
#             counterSNA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arraySN[0] = "B. Look for meaning and possibilities";
#             counterSNB++;
#         } else {
#             System.out.println("Select A or B");
#             test2();
#         }
#     }
#     public static void test3(){
#         System.out.println("A. Logical, thinking, questioning.\t\t\t B. Empathetic, feeling, accommodating");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayTF[0] = "A. Logical, thinking, questioning.";
#             counterTFA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayTF[0] = "B. Empathetic, feeling, accommodating";
#             counterTFB++;
#         }
#         else{
#             System.out.println("Select A or B ");
#             test3();
#         }
#
#     }
#     public static void test4(){
#         System.out.println("A. Organized, orderly.\t\t\t B. Flexible, adaptable");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayJP[0] = "A. Organized, orderly.";
#             counterJPA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayJP[0] ="B. Flexible, adaptable";
#             counterJPB++;
#         }
#         else {
#             System.out.println("Select an option");
#             test4();
#         }
#
#     }
#     public static void test5(){
#         System.out.println("A. More outgoing, think out loud.\t\t\t B. More reserved, think to yourself.");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayEI[2] = "A. More outgoing, think out loud.";
#             counterEIA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayEI[2] = "B. More reserved, think to yourself.";
#             counterEIB++;
#         }
#         else {
#             System.out.println("Select an option");
#             test5();
#         }
#     }
#      public static void test6(){
#          System.out.println("A. Practical, realistic, experiential. \t\t\t B. imagination, innovative, theoretical.");
#          System.out.println("Select an option");
#          String option = input.nextLine();
#          if (option.equalsIgnoreCase("A")){
#              arraySN[1] = "A. Practical, realistic, experiential.";
#              counterSNA++;
#          } else if (option.equalsIgnoreCase("B")) {
#              arraySN[1] = "B. Imagination, innovative, theoretical.";
#              counterSNB++;
#          }
#          else{
#              System.out.println("Select an option");
#              test6();
#
#              }
#     }
#
#     public static void test7(){
#         System.out.println("A. Candid, straight forward, frank. \t\t\t B. Tactful, kind, encouraging.");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayTF[1]  = "A. Candid, straight forward, frank.";
#             counterTFA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayTF[1]  = "B. Tactful, kind, encouraging.";
#             counterTFB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test7();
#         }
#     }
#
#     public static void test8(){
#         System.out.println("A. Plan, schedule. \t\t\t B. Unplanned, spontaneous");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayJP[1] = "A. Plan, schedule.";
#             counterJPA++;
#         }
#         else if (option.equalsIgnoreCase("B")) {
#             arrayJP[1] = "B. Unplanned, spontaneous";
#             counterJPB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test8();
#         }
#
#     }
#
#     public static void test9(){
#         System.out.println("A. seek many tasks, public activities, interaction with others \t\t B. seek private, solitary activities with quiet to concentrate.");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayEI[3] = "A. seek many tasks, public activities, interaction with others";
#             counterEIA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayEI[3] = "B. seek private, solitary activities with quiet to concentrate.";
#             counterEIB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test9();
#         }
#     }
#
#     public static void test10(){
#         System.out.println("A. standard, usual, conventional. \t\t\t B. different, novel, unique.");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arraySN[2] = "A. standard, usual, conventional.";
#             counterSNA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arraySN[2]= "B. different, novel, unique.";
#             counterSNB++;
#         }
#         else{
#             System.out.println("Select an option ");
#             test10();
#         }
#
#     }
#
#     public static void test11(){
#         System.out.println("A. firm, tend to criticize, hold the line.\t\t\t B. gentle, tend to appreciate, conciliate. ");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayTF[2] = "A. firm, tend to criticize, hold the line.";
#             counterTFA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayTF[2] = "B. gentle, tend to appreciate, conciliate. ";
#             counterTFB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test11();
#         }
#     }
#
#     public static void test12(){
#         System.out.println("A.regulated, structured.\t\t\t B. easygoing, live  and let live");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayJP[2] = "A.regulated, structured.";
#             counterJPA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayJP[2] = "B. easygoing, live  and let live";
#             counterJPB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test12();
#         }
#     }
#
#     public static void test13(){
#         System.out.println("A. external, communicative, express yourself. \t\t\t B. internal, reticent, keep to yourself. ");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayEI[4] = "A. external, communicative, express yourself.";
#             counterEIA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayEI[4] = "B. internal, reticent, keep to yourself. ";
#             counterEIB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test13();}
#     }
#
#     public static void test14(){
#         System.out.println("A. focus on here-and-now.\t\t\t B. look to the future, global perspective, \"big picture\"");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arraySN[3] = "A. focus on here-and-now.";
#             counterSNA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arraySN[3] = "B. look to the future, global perspective, \"big picture\"";
#             counterSNB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test14();
#         }
#
#     }
#
#     public static void test15(){
#         System.out.println("A. tough minded, just. \t\t\t B. tender-hearted, merciful");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayTF[3] = "A. tough minded, just.";
#             counterTFA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayTF[3] = "B. tender-hearted, merciful";
#             counterTFB++;
#         }
#         else {
#             System.out.println("Select an option");
#             test15();
#         }
#     }
#
#     public static void test16(){
#         System.out.println("A. preparation, plan ahead. \t\t\t B. go with the flow, adapt as you go.");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayJP[3] = "A. preparation, plan ahead.";
#             counterJPA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayJP[3] = "B. go with the flow, adapt as you go.";
#             counterJPB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test16();
#         }
#     }
#
#     public static void test17(){
#         System.out.println("A. active, initiate. \t\t\t B. reflective, deliberate");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayEI[5] = "A. active, initiate.";
#             counterEIA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayEI[5] = "B. reflective, deliberate";
#             counterEIB++;
#         }
#         else{
#             System.out.println("Select an option");
#             test17();
#         }
#
#     }
#     public static void test18() {
#         System.out.println("A.facts, things, \"what is\" \t\t\t B. ideas, dreams, 'what could be', philosophical");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")) {
#             arraySN[4] = "A. facts, things, \"what is\"";
#             counterSNA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arraySN[4] = "B. ideas, dreams, 'what could be', philosophical";
#             counterSNB++;
#         } else {
#             System.out.println("Select an option ");
#             test18();
#         }
#     }
#     public static void test19(){
#         System.out.println("A. matter of fact, issue oriented \t\t\t B. sensitive, people-oriented, compassionate");
#         System.out.println("Select an option");
#         String option = input.nextLine();
#         if (option.equalsIgnoreCase("A")){
#             arrayTF[4]  = "A. matter of fact, issue oriented ";
#             counterTFA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayTF[4]  = "B. sensitive, people-oriented, compassionate";
#             counterTFB++;
#         }
#         else {
#             System.out.println("Select an option");
#             test19();
#         }
#     }
#
#     public static void test20(){
#         System.out.println("A. control, govern  \t\t\t B.latitude, freedom");
#         System.out.println("Select an option ");
#         String option =input.nextLine();
#         if(option.equalsIgnoreCase("A")){
#             arrayJP[4] = "A. control, govern";
#             counterJPA++;
#         } else if (option.equalsIgnoreCase("B")) {
#             arrayJP[4] = "B. latitude, freedom";
#             counterJPB++;
#         }
#         else {
#             System.out.println("Select an option");
#             test20();
#         }
#     }
#
#     public static void displayResult(){
#         System.out.println(arrayEI[0]);
#
#         System.out.println(arrayEI[1] + "\n" + arrayEI[2] + "\n" + arrayEI[3] + "\n" + arrayEI[4] + "\n" + arrayEI[5]
#                 + "\n" + "Number of A selected : " + counterEIA +
#                 "\n" + "Number of B selected : " + counterEIB);
#         System.out.println();
#
#
#         System.out.println(arraySN[0] + "\n" + arraySN[1] + "\n" + arraySN[2] + "\n" + arraySN[3] + "\n" + arraySN[4]
#                + "\n" + "NUmber of A selected  : " + counterSNA +
#                 "\n" + "Number of B selected  : " + counterSNB);
#         System.out.println();
#
#         System.out.println(arrayTF[0] + "\n" + arrayTF[1] + "\n" + arrayTF[2] + "\n" + arrayTF[3] + "\n" + arrayTF[4]
#                + "\n" + "Number of A selected : " + counterTFA +
#                 "\n" + "Number of B selected : " + counterTFB);
#         System.out.println();
#
#         System.out.println(arrayJP[0] + "\n" + arrayJP[1] + "\n" + arrayJP[2] + "\n" + arrayJP[3] + "\n" + arrayJP[4]
#                 + "\n" + "Number of A selected : " + counterJPA +
#                 "\n" + "Number of B selected : " + counterJPB);
#
#         if (counterEIA > counterEIB) {
#             realPersonality += "E";
#         } else {
#             realPersonality += "I";
#         }
#
#         if (counterSNA > counterSNB) {
#             realPersonality += "S";
#         }else {
#             realPersonality += "N";
#         }
#         if (counterTFA > counterTFB){
#            realPersonality += "T";
#         }else{
#             realPersonality += "F";
#         }
#         if (counterJPA > counterJPB){
#             realPersonality += "J";
#         }else{
#             realPersonality += "P";
#         }
#         System.out.println();
#
#
#         switch (realPersonality) {
#             case "EFNJ" -> System.out.println("ENFJ personalites\n" +
#                     "A ENTJ (ENFJ) is a person with the Extraverted, Intuitive, Feeling, and Judging personality traits. These warm, forthright types love helping others, and they tend to have strong ideas and values. They back their perspective with the creative energy to achieve their goals.\n" +
#                     "\n" +
#                     "ENTJs (ENFJs) feel called to serve a greater purpose in life. Thoughtful and idealistic, these personality types strive to have a positive impact on other people and the world around them. They rarely shy away from an opportunity to do the right thing, even when doing so is far from easy.\n" +
#                     "\n" +
#                     "ENTJs are born leaders, which explains why these personalities can be found among many notable politicians, coaches, and teachers. Their passion and charisma allow them to inspire others not just in their careers but in every arena of their lives, including their relationships. Few things bring ENTJs a deeper sense of joy and fulfillment than guiding friends and loved ones to grow into their best selves.\n" +
#                     "\n" +
#                     "ENTJs tend to be vocal about their values, including authenticity and altruism. When something strikes them as unjust or wrong, they speak up. But they rarely come across as brash or pushy, as their sensitivity and insight guide them to speak in ways that resonate with others.\n" +
#                     "\n" +
#                     "People with this personality type are devoted altruists, ready to face slings and arrows in order to stand up for the people and ideas that they believe in. This strength of conviction bolsters ENTJs’ innate leadership skills, particularly their ability to guide people to work together in service of the greater good.");
#
#             case "ENTJ" -> System.out.println("ENTJ personalities\n" +
#                     "A (ENTJ) is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits. They are decisive people who love momentum and accomplishment. They gather information to construct their creative visions but rarely hesitate for long before acting on them. \n" +
#                     "If there’s anything ENTJs love,it’s a good challenge, big or small, and they firmly believe that given enough time and resources, they can achieve any goal. This quality makes people with the Commander personality type brilliant entrepreneurs, and their ability to think strategically and hold a long-term focus while executing each step of their plans with determination and precision makes them powerful business leaders.\n" +
#                     "\n" +
#                     " ENTJs see inefficiency not just as a problem in its own right, but as something that pulls time and energy away from all their future goals, an elaborate sabotage consisting of irrationality and laziness. People with the Commander personality type will root out such behavior wherever they go.\n" +
#                     "Energetic – Rather than finding this process taxing Commanders are energized by it, genuinely enjoying leading their teams forward as they implement their plans and goals.\n" +
#                     "ENTJ couldn’t do this if they were plagued by self-doubt – they trust their abilities, make known their opinions, and believe in their capacities as leaders.\n" +
#                     "Strong-Willed – Nor do they give up when the going gets tough – Commander personalities strive to achieve their goals, but really nothing is quite as satisfying to them as rising to the challenge of each obstacle in their run to the finish line.\n" +
#                     "ENTJ exemplify the difference between moment-to-moment crisis management and navigating the challenges and steps of a bigger plan, and are known for examining every angle of a problem and not just resolving momentary issues, but moving the whole project forward with their solutions. These qualities combine to create individuals who are able to inspire and invigorate others, who people actually want to be their leaders, and this in turn helps Commanders to accomplish their often ambitious goals that could never be finished alone.\n");
#
#             case "ENFP" -> System.out.println("\n" +
#                     "A ENFP (ENFP) is someone with the Extraverted, Intuitive, Feeling, and Prospecting personality traits. These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. Their vibrant energy can flow in many directions.\n" +
#                     "\n" +
#                     "It doesn’t interest me what you do for a living. I want to know what you ache for – and if you dare to dream of meeting your heart’s longing.\n" +
#                     "\n" +
#                     "ENFPs (ENFPs) are true free spirits – outgoing, openhearted, and open-minded. With their lively, upbeat approach to life, they stand out in any crowd. But even though they can be the life of the party, ENFPs don’t just care about having a good time. These personality types run deep – as does their longing for meaningful, emotional connections with other people.\n" +
#                     "\n" +
#                     "Friendly and outgoing, ENFPs are devoted to enriching their relationships and their social lives. But beneath their sociable, easygoing exteriors, they have rich, vibrant inner lives as well. Without a healthy dose of imagination, creativity, and curiosity, a ENFP simply wouldn’t be a ENFP.\n" +
#                     "\n" +
#                     "In their unique way, ENFPs can be quite introspective. They can’t help but ponder the deeper meaning and significance of life – even when they should be paying attention to something else. These personalities believe that everything – and everyone – is connected, and they live for the glimmers of insight that they can gain into these connections.\n" +
#                     "\n" +
#                     "ENFPs are independent and creative, always on the lookout for the magic and meaning in everyday life.\n" +
#                     "When something sparks their imagination, ENFPs can show an enthusiasm that is nothing short of infectious. These personalities radiate a positive energy that draws in other people, and ENFPs may find themselves being held up by their peers as a leader or guru. But once the initial bloom of inspiration wears off, ENFPs can struggle with self-discipline and consistency, losing steam on projects that once meant so much to them.\n" +
#                     "\n" +
#                     "Seeking Joy\n" +
#                     "ENFPs are proof that seeking out life’s joys and pleasures isn’t the same as being shallow. Seemingly in the blink of an eye, people with this personality type can transform from impassioned idealists to carefree figures on the dance floor.\n" +
#                     "\n" +
#                     "ENFP personalities are capable of intense thought and feeling – and also of kicking back and having a good time.\n" +
#                     "Even in moments of fun, ENFPs want to connect emotionally with others. Few things matter more to these personality types than having genuine, heartfelt conversations with the people they cherish. ENFPs believe that everyone deserves to express their feelings, and their empathy and warmth create spaces where even the most timid spirits can feel comfortable opening up.");
#
#             case "ENTP" -> System.out.println("ENTP personalities\n" +
#                     "\n" +
#                     "An (ENTP) is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.\n" +
#                     "Quick-witted and audacious, ENTP aren’t afraid to disagree with the status quo. In fact, they’re not afraid to disagree with pretty much anything or anyone. Few things light up people with this personality type more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much the better.\n" +
#                     "\n" +
#                     "ENTP are known for their rebellious streak. For this personality type, no belief is too sacred to be questioned, no idea is too fundamental to be scrutinized, and no rule is too important to be broken, or at least thoroughly tested. Sometimes ENTP even rebel against their own beliefs by arguing the opposing viewpoint – just to see how the world looks from the other side.\n" +
#                     "some of the weakness of the ENTP are that they have mental exercise of debating and to them, nothing is sacred. They often misjudge others feelings and push their debtates well past others tolerance level. sometimes this personalities find it difficult to focus.\n" +
#                     "some of the Strength of this personality is that hey are very knowledgeable, they are quick thinkers, and excellent brainstormers. Their confidence, quick thought and ability to connect disparate ideas in novel ways create a style of communication that is charming, even entertaining, and informative at the same time.");
#
#             case "ESFJ" -> System.out.println("ESFJ\n" +
#                     "\n" +
#                     "A ESFJ (ESFJ) is a person with the Extraverted, Observant, Feeling, and Judging personality traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.\n" +
#                     "\n" +
#                     "Encourage, lift, and strengthen one another. For the positive energy spread to one will be felt by us all.\n" +
#                     "\n" +
#                     "DEBORAH DAY\n" +
#                     "For ESFJs, life is sweetest when it’s shared with others. People with this personality type form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors.\n" +
#                     "\n" +
#                     "This doesn’t mean that ESFJs like everyone, or that they’re saints. But ESFJs do believe in the power of hospitality and good manners, and they tend to feel a sense of duty to those around them. Generous and reliable, people with this personality type often take it upon themselves – in ways both large and small – to hold their families and their communities together.\n" +
#                     "\n" +
#                     "ESFJs have a talent for making the people in their lives feel supported, cared for, and secure.\n" +
#                     "\n" +
#                     "The Beauty of a Responsible Life\n" +
#                     "ESFJs are altruists. They take seriously their responsibilities to give back, serve others, and do the right thing.\n" +
#                     "\n" +
#                     "And ESFJs believe that there is a clear right thing to do in nearly every situation. While some personality types adopt a more lenient, live-and-let-live attitude, ESFJs may find it difficult not to judge when someone takes a path that strikes them as misguided. As a result, ESFJs often struggle to accept it when someone – particularly someone they care about – disagrees with them.\n" +
#                     "\n" +
#                     "ESFJs have a clear moral compass – and it can be nothing short of baffling to them when other people’s actions don’t align with it.\n" +
#                     "With their definite views on right and wrong, ESFJs tend to be on the opinionated side. But these opinions aren’t arbitrary – they’re often based on a deep respect for tradition. ESFJs know that everything they do affects someone else, and they trust that established laws, protocols, and social norms will help them navigate their everyday lives in a way that is considerate and responsible toward others.\n" +
#                     "\n" +
#                     "Building Relationships That Last\n" +
#                     "Supportive and outgoing, ESFJs can always be spotted at a party – they’re the ones fluttering around making sure that everyone else is having a good time! But make no mistake: ESFJs don’t just breeze through other people’s lives. Loyal to the core, they build lasting relationships, and they can be counted on to show up whenever a helping hand – or a listening ear – is needed.\n" +
#                     "\n" +
#                     "ESFJs rarely miss a birthday or holiday. Devoted to their relationships, they commit even the smallest details of their friends’ and loved ones’ lives to memory.\n" +
#                     "With their love of order and structure, ESFJs prefer planned events to open-ended activities or spontaneous get-togethers – and they’re happy to host in order to ensure that everything goes smoothly. People with this personality type put a great deal of energy into making other people feel special and celebrated, and they may take it personally when someone doesn’t seem to appreciate their efforts.\n" +
#                     "\n" +
#                     "For many people with the ESFJ personality type, one of life’s greatest challenges is accepting that they can’t control anyone else’s thoughts or behavior – not even those who are nearest and dearest to them. Fortunately, ESFJs can find peace and fulfillment by focusing on what they do best: setting an example of care, consideration, and responsibility – and bringing people together in the process.");
#
#             case "ESFP" -> System.out.println("ESFJ\n" +
#                     "\n" +
#                     "A ESFJ (ESFJ) is a person with the Extraverted, Observant, Feeling, and Judging personality traits. They are attentive and people-focused, and they enjoy taking part in their social community. Their achievements are guided by decisive values, and they willingly offer guidance to others.\n" +
#                     "\n" +
#                     "Encourage, lift, and strengthen one another. For the positive energy spread to one will be felt by us all.\n" +
#                     "\n" +
#                     "DEBORAH DAY\n" +
#                     "For ESFJs, life is sweetest when it’s shared with others. People with this personality type form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors.\n" +
#                     "\n" +
#                     "This doesn’t mean that ESFJs like everyone, or that they’re saints. But ESFJs do believe in the power of hospitality and good manners, and they tend to feel a sense of duty to those around them. Generous and reliable, people with this personality type often take it upon themselves – in ways both large and small – to hold their families and their communities together.\n" +
#                     "\n" +
#                     "ESFJs have a talent for making the people in their lives feel supported, cared for, and secure.\n" +
#                     "\n" +
#                     "The Beauty of a Responsible Life\n" +
#                     "ESFJs are altruists. They take seriously their responsibilities to give back, serve others, and do the right thing.\n" +
#                     "\n" +
#                     "And ESFJs believe that there is a clear right thing to do in nearly every situation. While some personality types adopt a more lenient, live-and-let-live attitude, ESFJs may find it difficult not to judge when someone takes a path that strikes them as misguided. As a result, ESFJs often struggle to accept it when someone – particularly someone they care about – disagrees with them.\n" +
#                     "\n" +
#                     "ESFJs have a clear moral compass – and it can be nothing short of baffling to them when other people’s actions don’t align with it.\n" +
#                     "With their definite views on right and wrong, ESFJs tend to be on the opinionated side. But these opinions aren’t arbitrary – they’re often based on a deep respect for tradition. ESFJs know that everything they do affects someone else, and they trust that established laws, protocols, and social norms will help them navigate their everyday lives in a way that is considerate and responsible toward others.\n" +
#                     "\n" +
#                     "Building Relationships That Last\n" +
#                     "Supportive and outgoing, ESFJs can always be spotted at a party – they’re the ones fluttering around making sure that everyone else is having a good time! But make no mistake: ESFJs don’t just breeze through other people’s lives. Loyal to the core, they build lasting relationships, and they can be counted on to show up whenever a helping hand – or a listening ear – is needed.\n" +
#                     "\n" +
#                     "ESFJs rarely miss a birthday or holiday. Devoted to their relationships, they commit even the smallest details of their friends’ and loved ones’ lives to memory.\n" +
#                     "With their love of order and structure, ESFJs prefer planned events to open-ended activities or spontaneous get-togethers – and they’re happy to host in order to ensure that everything goes smoothly. People with this personality type put a great deal of energy into making other people feel special and celebrated, and they may take it personally when someone doesn’t seem to appreciate their efforts.\n" +
#                     "\n" +
#                     "For many people with the ESFJ personality type, one of life’s greatest challenges is accepting that they can’t control anyone else’s thoughts or behavior – not even those who are nearest and dearest to them. Fortunately, ESFJs can find peace and fulfillment by focusing on what they do best: setting an example of care, consideration, and responsibility – and bringing people together in the process.");
#
#             case "ESTJ" -> System.out.println("ESTJ\n" +
#                     "\n" +
#                     "An ESTJ (ESTJ) is someone with the Extraverted, Observant, Thinking, and Judging personality traits. They possess great fortitude, emphatically following their own sensible judgment. They often serve as a stabilizing force among others, able to offer solid direction amid adversity.\n" +
#                     "\n" +
#                     "Good order is the foundation of all things.\n" +
#                     "\n" +
#                     "EDMUND BURKE\n" +
#                     "ESTJs are representatives of tradition and order, utilizing their understanding of what is right, wrong and socially acceptable to bring families and communities together. Embracing the values of honesty, dedication and dignity, people with the ESTJ personality type are valued for their clear advice and guidance, and they happily lead the way on difficult paths. Taking pride in bringing people together, ESTJs often take on roles as community organizers, working hard to bring everyone together in celebration of cherished local events, or in defense of the traditional values that hold families and communities together.\n" +
#                     "\n" +
#                     "ESTJ (ESTJ) personality\n" +
#                     "Leading by Example\n" +
#                     "Demand for such leadership is high in democratic societies, and forming no less than 11% of the population, it’s no wonder that many of America’s presidents have been ESTJs. Strong believers in the rule of law and authority that must be earned, ESTJ personalities lead by example, demonstrating dedication and purposeful honesty, and an utter rejection of laziness and cheating, especially in work. If anyone declares hard, manual work to be an excellent way to build character, it is ESTJs.\n" +
#                     "\n" +
#                     "ESTJs are aware of their surroundings and live in a world of clear, verifiable facts – the surety of their knowledge means that even against heavy resistance, they stick to their principles and push an unclouded vision of what is and is not acceptable. Their opinions aren’t just empty talk either, as ESTJs are more than willing to dive into the most challenging projects, improving action plans and sorting details along the way, making even the most complicated tasks seem easy and approachable.\n" +
#                     "\n" +
#                     "However, ESTJs don’t work alone, and they expect their reliability and work ethic to be reciprocated – people with this personality type meet their promises, and if partners or subordinates jeopardize them through incompetence or laziness, or worse still, dishonesty, they do not hesitate to show their wrath. This can earn them a reputation for inflexibility, a trait shared by all Sentinel personalities, but it’s not because ESTJs are arbitrarily stubborn, but because they truly believe that these values are what make society work.\n" +
#                     "\n" +
#                     "A Greater Responsibility\n" +
#                     "ESTJs are classic images of the model citizen: they help their neighbors, uphold the law, and try to make sure that everyone participates in the communities and organizations they hold so dear.\n" +
#                     "The main challenge for ESTJs is to recognize that not everyone follows the same path or contributes in the same way. A true leader recognizes the strength of the individual, as well as that of the group, and helps bring those individuals’ ideas to the table. That way, ESTJs really do have all the facts, and are able to lead the charge in directions that work for everyone.");
#
#             case "ESTP" -> System.out.println("An ESTP \n" +
#                     "ESTP is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.\n" +
#                     "\n" +
#                     "ESTPs always have an impact on their immediate surroundings – the best way to spot them at a party is to look for the whirling eddy of people flitting about them as they move from group to group. Laughing and entertaining with a blunt and earthy humor, ESTP personalities love to be the center of attention. If an audience member is asked to come on stage, ESTPs volunteer – or volunteer a shy friend.\n" +
#                     "\n" +
#                     "Theory, abstract concepts and plodding discussions about global issues and their implications don’t keep ESTPs interested for long. ESTPs keep their conversation energetic, with a good dose of intelligence, but they like to talk about what is – or better yet, to just go out and do it. ESTPs leap before they look, fixing their mistakes as they go, rather than sitting idle, preparing contingencies and escape clauses.\n" +
#                     "\n" +
#                     "\n" +
#                     "Diving Right In\n" +
#                     "ESTPs are the likeliest personality type to make a lifestyle of risky behavior. They live in the moment and dive into the action – they are the eye of the storm. People with the ESTP personality type enjoy drama, passion, and pleasure, not for emotional thrills, but because it’s so stimulating to their logical minds. They are forced to make critical decisions based on factual, immediate reality in a process of rapid-fire rational stimulus response.\n" +
#                     "\n" +
#                     "This makes school and other highly organized environments a challenge for ESTPs. It certainly isn’t because they aren’t smart, and they can do well, but the regimented, lecturing approach of formal education is just so far from the hands-on learning that ESTPs enjoy. It takes a great deal of maturity to see this process as a necessary means to an end, something that creates more exciting opportunities.\n" +
#                     "\n" +
#                     "Also challenging is that to ESTPs, it makes more sense to use their own moral compass than someone else’s. Rules were made to be broken. This is a sentiment few high school instructors or corporate supervisors are likely to share, and can earn ESTP personalities a certain reputation. But if they minimize the trouble-making, harness their energy, and focus through the boring stuff, ESTPs are a force to be reckoned with.\n" +
#                     "\n" +
#                     "The Path Less Traveled\n" +
#                     "With perhaps the most perceptive, unfiltered view of any type, ESTPs have a unique skill in noticing small changes. Whether a shift in facial expression, a new clothing style, or a broken habit, people with this personality type pick up on hidden thoughts and motives where most types would be lucky to pick up anything specific at all. ESTPs use these observations immediately, calling out the change and asking questions, often with little regard for sensitivity. ESTPs should remember that not everyone wants their secrets and decisions broadcast.");
#
#             case "INFJ" ->
#                     System.out.println("An Advocate (INFJ) is someone with the Introverted, Intuitive, Feeling, and Judging personality traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.\n" +
#                             "\n" +
#                             "“Treat people as if they were what they ought to be and you help them to become what they are capable of being.”\n" +
#                             "\n" +
#                             "(INFJs) may be the rarest personality type of all, but they certainly leave their mark on the world. Idealistic and principled, they aren’t content to coast through life – they want to stand up and make a difference. For Advocate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world.\n" +
#                             "\n" +
#                             "While they have lofty goals and ambitions, INFJs shouldn’t be mistaken for idle dreamers. People with this personality type care about integrity, and they’re rarely satisfied until they’ve done what they know to be right. Conscientious to the core, they move through life with a clear sense of their values, and they aim never to lose sight of what truly matters – not according to other people or society at large, but according to their own wisdom and intuition.\n" +
#                             "\n" +
#                             "Perhaps because their personality type is so uncommon, INFJs tend to carry around a sense – whether conscious or not – of being different from most people. With their rich inner lives and their deep, abiding desire to find their life purpose, they don’t always fit in with those around them. This isn’t to say that Advocates can’t enjoy social acceptance or close relationships – only that they sometimes feel misunderstood or at odds with the world.\n" +
#                             "\n" +
#                             "INFJ may be Introverted, but they value deep, authentic relationships with others. Few things bring these personalities as much joy as truly knowing another person – and being known in return. Advocates enjoy meaningful conversations far more than small talk, and they tend to communicate in a way that is warm and sensitive");
#
#             case "INFP" ->
#                     System.out.println("A  (INFP) is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality traits. These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.\n" +
#                             "\n" +
#                             "Although they may seem quiet or unassuming,  (INFPs) have vibrant, passionate inner lives. Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their minds. These personalities are known for their sensitivity – INFP can have profound emotional responses to music, art, nature, and the people around them.\n" +
#                             "\n" +
#                             "Idealistic and empathetic, INFP long for deep, soulful relationships, and they feel called to help others. But because this personality type makes up such a small portion of the population, INFPs may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits that make them unique.\n" +
#                             "\n" +
#                             "Empathy is among this personality type’s greatest gifts, but at times it can be a liability. The troubles of the world weigh heavily on INFP’ shoulders, and these personalities can be vulnerable to internalizing other people’s negative moods or mindsets. Unless they learn to set boundaries, INFP may feel overwhelmed by just how many wrongs there are that need to be set right.\n" +
#                             "\n" +
#                             "People with this personality type tend to feel directionless or stuck until they connect with a sense of purpose for their lives. For many INFP, this purpose has something to do with uplifting others and their ability to feel other people’s suffering as if it were their own. While INFP want to help everyone, they need to focus their energy and efforts – otherwise, they can end up exhausted.");
#
#             case "INTJ" -> System.out.println("INTJ pesonality type\n" +
#                     "An INTJ is a person with the Introverted, Intuitive, Thinking, and Judging personality traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.\n" +
#                     "Rational and quick-witted, INTJs pride themselves on their ability to think for themselves, not to mention their uncanny knack for seeing right through phoniness and hypocrisy. But because their minds are never at rest, Architects may struggle to find people who can keep up with their nonstop analysis of everything around them.\n" +
#                     "\n" +
#                     "This personality type comes with a strong independent streak. INTJs don’t mind acting alone, perhaps because they don’t like waiting around for others to catch up with them. They also generally prefer making decisions without asking for anyone else’s input. At times, this lone-wolf behavior can come across as insensitive, as it fails to take into consideration other people’s thoughts, desires, and plans.\n" +
#                     "\n" +
#                     "Architects contemplate the strengths and weaknesses of each move before they make it. And they never lose faith that, with enough ingenuity and insight, they can find a way to win – no matter what challenges might arise along the way.\n" +
#                     "\n" +
#                     "INTJ personalities can be rational, informed, independent, determined curious, and original. And some are their weaknesses is that they are arogant, dismissive of  emotions, Overly Critical, Combative, Socially Clueless.");
#
#             case "INTP" -> System.out.println("INTP personalities\n" +
#                     "A (INTP) is someone with the Introverted, Intuitive, Thinking, and Prospecting personality traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.\n" +
#                     "INTP often lose themselves in thought – which isn’t necessarily a bad thing. People with this personality type hardly ever stop thinking. From the moment they wake up, their minds buzz with ideas, questions, and insights. At times, they may even find themselves conducting full-fledged debates in their own heads.\n" +
#                     "People with this personality type want to understand everything in the universe, but one area in particular tends to mystify them: human nature. As their name suggests, Logicians feel most at home in the realm of logic and rationality. As a result, they can find themselves baffled by the illogical, irrational ways that feelings and emotions influence people’s behavior – including their own.\n" +
#                     "\n" +
#                     "Some of this personality strength is that they analyze everything that they come across, from research data to the behavior of the people around them. Thanks to their unrelenting imagination, Logicians can come up with creative, counterintuitive ideas that wouldn’t occur to most people. Logicians are driven by curiosity and an intense desire to learn everything that they can. These personalities are always casting about for new pursuits, hobbies, and areas of research. they care about the truth. Rather than taking comfort in ideology or received ideas, they want to understand what’s really going on beneath the surface of things.");
#
#             case "ISFJ" -> System.out.println("ISFJ\n" +
#                     "A ISFJ () is someone with the Introverted, Observant, Feeling, and Judging personality traits. These people tend to be warm and unassuming in their own steady way. They’re efficient and responsible, giving careful attention to practical details in their daily lives.\n" +
#                     "\n" +
#                     "Love only grows by sharing. You can only have more for yourself by giving it away to others.\n" +
#                     "\n" +
#                     "BRIAN TRACY\n" +
#                     "In their unassuming, understated way, ISFJs help make the world go round. Hardworking and devoted, people with this personality type feel a deep sense of responsibility to those around them. ISFJs can be counted on to meet deadlines, remember birthdays and special occasions, uphold traditions, and shower their loved ones with gestures of care and support. But they rarely demand recognition for all that they do, preferring instead to operate behind the scenes.\n" +
#                     "\n" +
#                     "This is a capable, can-do personality type, with a wealth of versatile gifts. Though sensitive and caring, ISFJs also have excellent analytical abilities and an eye for detail. And despite their reserve, they tend to have well-developed people skills and robust social relationships. ISFJs are truly more than the sum of their parts, and their varied strengths shine in even the most ordinary aspects of their daily lives.\n" +
#                     "\n" +
#                     "ISFJs are true altruists, meeting kindness with kindness-in-excess and engaging with the work and people they believe in with enthusiasm and generosity.\n" +
#                     "\n" +
#                     "The Gift of Loyalty\n" +
#                     "Among ISFJs’ most distinctive traits is loyalty. Rare is the ISFJ who allows a friendship or relationship to fade away from lack of effort. Instead, they invest a great deal of energy into maintaining strong connections with their loved ones – and not just by sending “How are you doing?” texts. People with this personality type are known for dropping everything and lending a hand whenever a friend or family member is going through a hard time.\n" +
#                     "\n" +
#                     "ISFJs tend to feel most energized and effective when they’re showing up for someone who needs their help.\n" +
#                     "ISFJs’ sense of loyalty doesn’t stop with their nearest and dearest – it often extends to their communities, their employers, and even family traditions. But the intensity of their commitment and desire to serve can have its downsides. Other people may take advantage of ISFJs’ helpful, hardworking nature, leaving them feeling burned out and overworked. And ISFJs may feel guilty or stressed when they contemplate changes – even necessary changes – to themselves, their relationships, or the way they’ve done things in the past.\n" +
#                     "\n" +
#                     "The Highest of Standards\n" +
#                     "For ISFJs, “good enough” is rarely good enough. People with this personality type can be meticulous to the point of perfectionism. They take their responsibilities personally, consistently going above and beyond and doing everything that they can to exceed others’ expectations.\n" +
#                     "\n" +
#                     "ISFJ personalities are known for their humility, and they rarely seek the spotlight.\n" +
#                     "But what happens when ISFJs’ efforts go unnoticed or unappreciated? While ISFJs tend to underplay their accomplishments, that doesn’t mean that they don’t enjoy recognition – or that they’re fine with being taken for granted. Unless they learn to stand up for themselves, ISFJs may find themselves quietly losing their enthusiasm and motivation, eventually becoming resentful toward the people who just don’t seem to appreciate them.\n" +
#                     "\n" +
#                     "Showing Up for Others – and Themselves\n" +
#                     "Although they’re Introverted, ISFJs have a deeply social nature. Thanks to their ability to remember the details of other people’s lives, ISFJs have a special talent for making their friends and acquaintances feel seen, known, and cherished. Few personality types can match ISFJs’ ability to choose just the right gift for any occasion, whether large or small.\n" +
#                     "\n" +
#                     "Dedicated and thoughtful, ISFJs find great joy in helping those around them build stable, secure, and happy lives. It may not be easy for people with this personality type to show up for themselves in the way that they show up for other people, but when they do, they often find themselves with even more energy and motivation to do good in the world.");
#
#             case "" ->
#                     System.out.println("An ISFP (ISFP) is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. They tend to have open minds, approaching life, new experiences, and people with grounded warmth. Their ability to stay in the moment helps them uncover exciting potentials.\n" +
#                             "\n" +
#                             "I change during the course of a day. I wake and I’m one person, and when I go to sleep I know for certain I’m somebody else.\n" +
#                             "\n" +
#                             "BOB DYLAN\n" +
#                             "ISFPs are true artists – although not necessarily in the conventional sense. For this personality type, life itself is a canvas for self-expression. From what they wear to how they spend their free time, ISFPs act in ways that vividly reflect who they are as unique individuals.\n" +
#                             "\n" +
#                             "And every ISFP is certainly unique. Driven by curiosity and eager to try new things, people with this personality often have a fascinating array of passions and interests. With their exploratory spirits and their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet. The only irony? Unassuming and humble, ISFPs tend to see themselves as “just doing their own thing,” so they may not even realize how remarkable they really are.\n" +
#                             "\n" +
#                             "\n" +
#                             "The Beauty of an Open Mind\n" +
#                             "ISFPs embrace a flexible, adaptable approach to life. Some personality types thrive on strict schedules and routines – but not ISFPs. ISFPs take each day as it comes, doing what feels right to them in the moment. And they make sure to leave plenty of room in their lives for the unexpected – with the result that many of their most cherished memories are of spontaneous, spur-of-the-moment outings and adventures, whether by themselves or with their loved ones.\n" +
#                             "\n" +
#                             "This flexible mindset makes ISFPs remarkably tolerant and open-minded. These personalities genuinely love living in a world filled with all kinds of people – even people who disagree with them or choose radically different lifestyles. It’s no surprise, then, that ISFPs are unusually open to changing their minds and rethinking their opinions. If any personality type believes in giving something (or someone) a second chance, it’s ISFPs.\n" +
#                             "\n" +
#                             "ISFPs want to live in a world where they – and everyone else – have the freedom to live as they see fit, without judgment.\n" +
#                             "That said, ISFPs’ go-with-the-flow mentality can have its downsides. People with this personality type may struggle to set long-term plans – let alone stick with them. As a result, ISFPs tend to have a pretty cloudy view of their ability to achieve their goals, and they often worry about letting other people down. ISFPs may find that adding a little structure to their lives goes a long way toward helping them feel more capable and organized – without quashing their independent spirits.\n" +
#                             "\n" +
#                             "Living in Harmony\n" +
#                             "In their relationships, ISFPs are warm, friendly, and caring, taking wholehearted enjoyment in the company of their nearest and dearest. But make no mistake: this is an Introverted personality type, meaning that ISFPs need dedicated alone time to recharge their energy after socializing with others. This alone time is what allows ISFPs to reestablish a sense of their own identity – in other words, to reconnect with who they truly are.");
#
#             case "ISTP" -> System.out.println(" ISTP \n" +
#                     " ISTP is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.\n" +
#                     "\n" +
#                     "I wanted to live the life, a different life. I didn’t want to go to the same place every day and see the same people and do the same job. I wanted interesting challenges.\n" +
#                     "\n" +
#                     "HARRISON FORD\n" +
#                     "ISTPs love to explore with their hands and their eyes, touching and examining the world around them with cool rationalism and spirited curiosity. People with this personality type are natural Makers, moving from project to project, building the useful and the superfluous for the fun of it, and learning from their environment as they go. Often mechanics and engineers, ISTPs find no greater joy than in getting their hands dirty pulling things apart and putting them back together, just a little bit better than they were before.\n" +
#                     "\n" +
#                     "\n" +
#                     "ISTPs explore ideas through creating, troubleshooting, trial and error and first-hand experience. They enjoy having other people take an interest in their projects and sometimes don’t even mind them getting into their space. Of course, that’s on the condition that those people don’t interfere with ISTPs’ principles and freedom, and they’ll need to be open to ISTPs returning the interest in kind.\n" +
#                     "\n" +
#                     "ISTPs enjoy lending a hand and sharing their experience, especially with the people they care about, and it’s a shame they’re so uncommon, making up only about five percent of the population. ISTP women are especially rare, and the typical gender roles that society tends to expect can be a poor fit – they’ll often be seen as tomboys from a young age.\n" +
#                     "\n" +
#                     "Dare to Differ\n" +
#                     "While their mechanical tendencies can make them appear simple at a glance, ISTPs are actually quite enigmatic. Friendly but very private, calm but suddenly spontaneous, extremely curious but unable to stay focused on formal studies, ISTP personalities can be a challenge to predict, even by their friends and loved ones. ISTPs can seem very loyal and steady for a while, but they tend to build up a store of impulsive energy that explodes without warning, taking their interests in bold new directions.\n" +
#                     "\n" +
#                     "Rather than some sort of vision quest though, ISTPs are merely exploring the viability of a new interest when they make these seismic shifts.\n" +
#                     "ISTPs’ decisions stem from a sense of practical realism, and at their heart is a strong sense of direct fairness, a “do unto others” attitude, which really helps to explain many of ISTPs’ puzzling traits. Instead of being overly cautious though, avoiding stepping on toes in order to avoid having their toes stepped on, ISTPs are likely to go too far, accepting likewise retaliation, good or bad, as fair play.\n" +
#                     "\n" +
#                     "The biggest issue ISTPs are likely to face is that they often act too soon, taking for granted their permissive nature and assuming that others are the same. They’ll be the first to tell an insensitive joke, get overly involved in someone else’s project, roughhouse and play around, or suddenly change their plans because something more interesting came up.\n" +
#                     "\n" +
#                     "Defying the Rules\n" +
#                     "ISTPs will come to learn that many other personality types have much more firmly drawn lines on rules and acceptable behavior than they do – they don’t want to hear an insensitive joke, and certainly wouldn’t tell one back, and they wouldn’t want to engage in horseplay, even with a willing party. If a situation is already emotionally charged, violating these boundaries can backfire tremendously.\n" +
#                     "\n" +
#                     "ISTPs have a particular difficulty in predicting emotions, but this is just a natural extension of their fairness, given how difficult it is to gauge ISTPs’ emotions and motivations. However, their tendency to explore their relationships through their actions rather than through empathy can lead to some very frustrating situations. People with the ISTP personality type struggle with boundaries and guidelines, preferring the freedom to move about and color outside the lines if they need to.\n" +
#                     "\n" +
#                     "Finding an environment where they can work with good friends who understand their style and unpredictability, combining their creativity, sense of humor and hands-on approach to build practical solutions and things, will give ISTPs many happy years of building useful boxes – and admiring them from the outside.");
#
#             case "ISTJ" -> System.out.println("ISTJ\n" +
#                     "A Logistician (ISTJ) is someone with the Introverted, Observant, Thinking, and Judging personality traits. These people tend to be reserved yet willful, with a rational outlook on life. They compose their actions carefully and carry them out with methodical purpose.\n" +
#                     "\n" +
#                     "ISTJ pride themselves on their integrity. People with this personality type mean what they say, and when they commit to doing something, they make sure to follow through.\n" +
#                     "\n" +
#                     "This personality type makes up a good portion of the overall population, and while ISTJ may not be particularly flashy or attention-seeking, they do more than their share to keep society on a sturdy, stable foundation. In their families and their communities, ISTJ often earn respect for their reliability, their practicality, and their ability to stay grounded and logical, even in the most stressful situations.\n" +
#                     "\n" +
#                     "The core of ISTJ’ self-respect comes from a sense of personal integrity. People with this personality type believe that there is a right way to proceed in any situation – and that anyone who pretends otherwise is probably trying to bend the rules to suit their own purposes. ISTJ have a deep respect for structure and tradition, and they are often drawn to organizations, workplaces, and educational settings that offer clear hierarchies and expectations.\n" +
#                     "\n" +
#                     "For many ISTJ, a lack of structure offers not freedom, but chaos.\n" +
#                     "People with the Logistician personality type rarely hesitate to take responsibility for their actions and choices. Generally speaking, they are quick to own up to their own mistakes, admitting the truth even if it doesn’t make them look good. To ISTJ, honesty is far more important than showmanship, and they’d rather satisfy their own conscience than lie to impress someone else.\n" +
#                     "\n" +
#                     "ISTJ’ dedication is an admirable quality, and it drives many of their accomplishments. But it can also become a weakness that other people take advantage of. With their strong work ethic and sense of duty, ISTJ may routinely find themselves shouldering other people’s responsibilities. Even if they don’t complain about the situation, ISTJ can end up exhausted or discouraged if they’re constantly expected – or taking it upon themselves – to pick up the slack for their colleagues, friends, or loved ones.");
#         }
#     }
#
#
#
#
#
#
#     }
#
