print('Привет! Это Тест 8. Инструкция к тесту: Этот вопросник предназначен для определения типичных способов  поведения и личностных характеристик. Он состоит из 70 утверждений (вопросов), \n каждое из которых имеет два варианта ответа. Вам необходимо выбрать ОДИН. Все ответы равноценны, среди них нет "правильных" или "неправильных"! Поэтому не нужно "угадывать" ответ. Выберите ответ, \n который свойствен вашему поведению в большинстве жизненных ситуаций. Работайте последовательно, не пропуская вопросов. Отвечайте правдиво, если вы хотите узнать что-то о себе, \n а не о какой-то мифической личности.')
user_name = input('Введите ваше имя:')
mail_name = input('Введите вашу почту:')
print('Начнём? Ответьте на 70 вопросов, обычно это занимает 3-5 минут.')

i = 0

user_ie = 0
user_sn = 0
user_tf = 0
user_jp = 0

user_i = 'I'
user_n = 'N'
user_f = 'F'
user_p = 'P'

user_full = 'Полное описание'

user_naber_ = ['',
                '1. В компании (на вечеринке) Вы a) общаетесь со многими, включая и незнакомцев б) общаетесь с немногими - Вашими знакомыми. \n Введите ответ: ',
                '2. Вы человек скорее а) реалистичный, чем склонный теоретизировать б) склонный теоретизировать, чем реалистичный. \n Введите ответ: ',
                '3. По-вашему, что хуже: а) витать в облаках б) придерживаться проторенной дорожки. \n Введите ответ: ',
                '4. Вы более подвержены влиянию а) принципов, законов б) эмоций, чувств. \n Введите ответ: ',
                '5. Вы более склонны а) убеждать б) затрагивать чувства. \n Введите ответ: ',
                '6. Вы предпочитаете работать а) выполняя все точно в срок б) не связывая себя определенными сроками. \n Введите ответ: ',
                '7. Вы склонны делать выбор а) довольно осторожно б) внезапно, импульсивно. \n Введите ответ: ',
                '8. В компании (на вечеринке) Вы а) остаетесь допоздна, не чувствуя усталости б) быстро утомляетесь и предпочитаете пораньше уйти.\n Введите ответ: ',
                '9. Вас более привлекают а) здравомыслящие люди б) люди с богатым воображением.\n Введите ответ: ',
                '10. Вам интересно а) то, что происходит в действительности б) те события, которые могут произойти.\n Введите ответ: ',
                '11. Оценивая поступки людей, Вы больше учитываете а) требования закона, чем обстоятельства б) обстоятельства, чем требования закона.\n Введите ответ: ',
                '12. Обращаясь к другим, Вы склонны а) соблюдать формальности, этикет б) проявлять свои личные, индивидуальные качества.\n Введите ответ: ',
                '13. Вы человек скорее а) точный, пунктуальный б) неторопливый, медлительный.\n Введите ответ: ',
                '14. Вас больше беспокоит необходимость а) оставлять дела незаконченными б) непременно доводить дела до конца.\n Введите ответ: ',
                '15. В кругу знакомых Вы, как правило а) в курсе происходящих событий б) узнаете о новостях с опозданием.\n Введите ответ: ',
                '16. Повседневные дела Вам нравится делать а) общепринятым способом б) своим оригинальным способом.\n Введите ответ: ',
                '17. Предпочитаю таких писателей, которые а) выражаются буквально, напрямую б) пользуются аналогиями, иносказаниями.\n Введите ответ: ',
                '18. Что Вас больше привлекает а) стройность мысли б) гармония человеческих отношений.\n Введите ответ: ',
                '19. Вы чувствуете себя увереннее а) в логических умозаключениях б) в практических оценках ситуаций.\n Введите ответ: ',
                '20. Вы предпочитаете, когда дела а) решены и устроены б) не решены и пока не улажены.\n Введите ответ: ',
                '21. Как по-вашему, Вы человек, скорее а) серьезный, определенный б) беззаботный, беспечный.\n Введите ответ: ',
                '22. При телефонных разговорах Вы а) заранее не продумываете все, что нужно сказать б) мысленно репетируете то, что будет сказано.\n Введите ответ: ',
                '23. Как Вы считаете, факты а) важны сами по себе б) есть проявления общих закономерностей.\n Введите ответ: ',
                '24. Фантазеры, мечтатели обычно а) раздражают Вас б) довольно симпатичны Вам.\n Введите ответ: ',
                '25. Вы чаще действуете как человек а) хладнокровный б) вспыльчивый, горячий.\n Введите ответ: ',
                '26. Как по-вашему, хуже быть а) несправедливым б) беспощадным.\n Введите ответ: ',
                '27. Обычно Вы предпочитаете действовать а) тщательно взвесив все возможности б) полагаясь на волю случая.\n Введите ответ: ',
                '28. Вам приятнее а) покупать что-нибудь б) иметь возможность купить.\n Введите ответ: ',
                '29. В компании Вы, как правило а) первым заводите беседу б) ждете, когда с Вами заговорят.\n Введите ответ: ',
                '30. Здравый смысл а) редко ошибается б) часто попадает впросак.\n Введите ответ: ',
                '31. Детям часто не хватает а) практичности б) воображения.\n Введите ответ: ',
                '32. В принятии решений Вы руководствуетесь скорее а) принятыми нормами б) своими чувствами, ощущениями.\n Введите ответ: ',
                '33. Вы человек скорее а) твердый, чем мягкий б) мягкий, чем твердый.\n Введите ответ: ',
                '34. Что, по-вашему, больше впечатляет а) умение методично организовать б) умение приспособиться и довольствоваться достигнутым.\n Введите ответ: ',
                '35. Вы больше цените а) определенность, законченность б) открытость, многовариантность.\n Введите ответ: ',
                '36. Новые и нестандартные отношения с людьми а) стимулируют, придают Вам энергии б утомляют Вас.\n Введите ответ: ',
                '37. Вы чаще действуете как а) человек практического склада б) человек оригинальный, необычный.\n Введите ответ: ',
                '38. Вы более склонны а) находить пользу в отношениях с людьми б) понимать мысли и чувства других.\n Введите ответ: ',
                '39. Что приносит Вам больше удовлетворения а) тщательное и всесторонне обсуждение спорного вопроса б) достижение соглашения по поводу спорного вопроса.\n Введите ответ: ',
                '40. Вы руководствуетесь более а) рассудком б) велениями сердца.\n Введите ответ: ',
                '41. Вам удобнее выполнять работу а) по предварительной договоренности б) которая подвернулась случайно.\n Введите ответ: ',
                '42. Вы обычно полагаетесь а) на организованность, порядок б) на случайность, неожиданность.\n Введите ответ: ',
                '43. Вы предпочитаете иметь а) много друзей на непродолжительный срок б) несколько старых друзей.\n Введите ответ: ',
                '44. Вы руководствуетесь в большей степени а) фактами, обстоятельствами б) общими положениями, принципами.\n Введите ответ: ',
                '45. Вас больше интересуют а) производство и сбыт продукции б) проектирование и исследования.\n Введите ответ: ',
                '46. Что Вы считаете за комплимент а) *Вот очень логичный человек* б) *Вот тонко чувствующий человек*.\n Введите ответ: ',
                '47. Вы более цените в себе а) невозмутимость б) увлеченность.\n Введите ответ: ',
                '48. Вы предпочитаете высказывать а) окончательные и определенные утверждения б) предварительные и неоднозначные утверждения.\n Введите ответ: ',
                '49. Вы лучше чувствуете себя а) после принятия решения б) не ограничивая себя решениями.\n Введите ответ: ',
                '50. Общаясь с незнакомыми, Вы а) легко завязываете продолжительные беседы б) не всегда находите общие темы для разговора.\n Введите ответ: ',
                '51. Вы больше доверяете а) своему опыту б) своим предчувствиям.\n Введите ответ: ',
                '52. Вы чувствуете себя человеком а) более практичным, чем изобретательным б) более изобретательным, чем практичным.\n Введите ответ: ',
                '53. Кто заслуживает большего одобрения - а) рассудительный, здравомыслящий человек б) человек, глубоко переживающий.\n Введите ответ: ',
                '54. Вы более склонны а) быть прямым и беспристрастным б) сочувствовать людям.\n Введите ответ: ',
                '55. Что, по-вашему, предпочтительней а) удостовериться, что все подготовлено и улажено б) предоставить событиям идти своим чередом.\n Введите ответ: ',
                '56. Отношения между людьми должны строиться а) на предварительной взаимной договоренности б) в зависимости от обстоятельств.\n Введите ответ: ',
                '57. Когда звонит телефон, Вы а) торопитесь подойти первым б) надеетесь, что подойдет кто-нибудь другой.\n Введите ответ: ',
                '58. Что Вы цените в себе больше а) развитое чувство реальности б) пылкое воображение.\n Введите ответ: ',
                '59. Вы больше придаете значение а) тому, что сказано б) тому, как сказано.\n Введите ответ: ',
                '60. Вы в основном считаете себя а) трезвым и практичным б) сердечным и отзывчивым.\n Введите ответ: ',
                '61. Что выглядит большим заблуждением а) излишняя пылкость, горячность б) чрезмерная объективность, беспристрастность.\n Введите ответ: ',
                '62. Какие ситуации привлекают Вас больше а) регламентированные и упорядоченные б) неупорядоченные и нерегламентированные.\n Введите ответ: ',
                '63. Вы человек, скорее а) педантичный, чем капризный б) капризный, чем педантичный.\n Введите ответ: ',
                '64. Вы чаще склонны а) быть открытым, доступным людям б) быть сдержанным, скрытным.\n Введите ответ: ',
                '65. В литературных произведениях Вы предпочитаете а) буквальность, конкретность б) образность, переносный смысл.\n Введите ответ: ',
                '66. Что для Вас труднее а) находить общий язык с другими б) использовать других в своих интересах.\n Введите ответ: ',
                '67. Чего бы вы себе больше пожелали а) ясности размышлений б) умения сочувствовать.\n Введите ответ: ',
                '68. Что хуже а) быть неприхотливым б) быть излишне привередливым.\n Введите ответ: ',
                '69. Вы предпочитаете а) запланированные события б) незапланированные события.\n Введите ответ: ','70. Вы склонны поступать скорее а) обдуманно, чем импульсивно б) импульсивно, чем обдуманно.\n Введите ответ: '
            ]

def user_naber_func(user_naber):
    user_naber = input(user_naber)
    while user_naber != 'а' and user_naber != 'б':
        print("Введите ответ а или б!")
        user_naber = input()
    return user_naber

def user_ie_func(user_naber, user_nn):
    if user_naber == 'а':
        user_nn = user_nn + 1
    return user_nn

for i in range(1,71):
    user_naber_[i] = user_naber_func(user_naber_[i])
    i += 1

user_ie = user_ie_func(user_naber_[1], user_ie)
user_ie = user_ie_func(user_naber_[8], user_ie)
user_ie = user_ie_func(user_naber_[15], user_ie)
user_ie = user_ie_func(user_naber_[22], user_ie)
user_ie = user_ie_func(user_naber_[29], user_ie)
user_ie = user_ie_func(user_naber_[36], user_ie)
user_ie = user_ie_func(user_naber_[43], user_ie)
user_ie = user_ie_func(user_naber_[50], user_ie)
user_ie = user_ie_func(user_naber_[57], user_ie)
user_ie = user_ie_func(user_naber_[64], user_ie)

user_sn = user_ie_func(user_naber_[2], user_sn)
user_sn = user_ie_func(user_naber_[3], user_sn)
user_sn = user_ie_func(user_naber_[9], user_sn)
user_sn = user_ie_func(user_naber_[10], user_sn)
user_sn = user_ie_func(user_naber_[16], user_sn)
user_sn = user_ie_func(user_naber_[17], user_sn)
user_sn = user_ie_func(user_naber_[23], user_sn)
user_sn = user_ie_func(user_naber_[24], user_sn)
user_sn = user_ie_func(user_naber_[30], user_sn)
user_sn = user_ie_func(user_naber_[31], user_sn)
user_sn = user_ie_func(user_naber_[37], user_sn)
user_sn = user_ie_func(user_naber_[38], user_sn)
user_sn = user_ie_func(user_naber_[44], user_sn)
user_sn = user_ie_func(user_naber_[45], user_sn)
user_sn = user_ie_func(user_naber_[51], user_sn)
user_sn = user_ie_func(user_naber_[52], user_sn)
user_sn = user_ie_func(user_naber_[58], user_sn)
user_sn = user_ie_func(user_naber_[59], user_sn)
user_sn = user_ie_func(user_naber_[65], user_sn)
user_sn = user_ie_func(user_naber_[66], user_sn)

user_tf = user_ie_func(user_naber_[4], user_tf)
user_tf = user_ie_func(user_naber_[5], user_tf)
user_tf = user_ie_func(user_naber_[11], user_tf)
user_tf = user_ie_func(user_naber_[12], user_tf)
user_tf = user_ie_func(user_naber_[18], user_tf)
user_tf = user_ie_func(user_naber_[19], user_tf)
user_tf = user_ie_func(user_naber_[25], user_tf)
user_tf = user_ie_func(user_naber_[26], user_tf)
user_tf = user_ie_func(user_naber_[32], user_tf)
user_tf = user_ie_func(user_naber_[33], user_tf)
user_tf = user_ie_func(user_naber_[39], user_tf)
user_tf = user_ie_func(user_naber_[40], user_tf)
user_tf = user_ie_func(user_naber_[46], user_tf)
user_tf = user_ie_func(user_naber_[47], user_tf)
user_tf = user_ie_func(user_naber_[53], user_tf)
user_tf = user_ie_func(user_naber_[54], user_tf)
user_tf = user_ie_func(user_naber_[60], user_tf)
user_tf = user_ie_func(user_naber_[61], user_tf)
user_tf = user_ie_func(user_naber_[67], user_tf)
user_tf = user_ie_func(user_naber_[68], user_tf)

user_jp = user_ie_func(user_naber_[6], user_jp)
user_jp = user_ie_func(user_naber_[7], user_jp)
user_jp = user_ie_func(user_naber_[13], user_jp)
user_jp = user_ie_func(user_naber_[14], user_jp)
user_jp = user_ie_func(user_naber_[20], user_jp)
user_jp = user_ie_func(user_naber_[21], user_jp)
user_jp = user_ie_func(user_naber_[27], user_jp)
user_jp = user_ie_func(user_naber_[28], user_jp)
user_jp = user_ie_func(user_naber_[34], user_jp)
user_jp = user_ie_func(user_naber_[35], user_jp)
user_jp = user_ie_func(user_naber_[41], user_jp)
user_jp = user_ie_func(user_naber_[42], user_jp)
user_jp = user_ie_func(user_naber_[48], user_jp)
user_jp = user_ie_func(user_naber_[49], user_jp)
user_jp = user_ie_func(user_naber_[55], user_jp)
user_jp = user_ie_func(user_naber_[56], user_jp)
user_jp = user_ie_func(user_naber_[62], user_jp)
user_jp = user_ie_func(user_naber_[63], user_jp)
user_jp = user_ie_func(user_naber_[69], user_jp)
user_jp = user_ie_func(user_naber_[70], user_jp)

if user_ie > 5:
    user_i = 'E'
else:
    user_i = 'I'

if user_sn > 10:
    user_n = 'S'
else:
    user_n = 'N'

if user_tf > 10:
    user_f = 'T'
else:
    user_f = 'F'

if user_jp > 10:
    user_p = 'J'
else:
    user_p = 'P'

user_nnnn = user_i + user_n + user_f + user_p

print(f'Буквенный код оценки: {user_nnnn} , Вашей оценкой является балл: {user_ie} {user_sn} {user_tf} {user_jp}')

if user_nnnn == 'ESTJ':
    user_full = 'Тип Администратор: ответственный, надежный для него важны долг, иерархия, порядок практичный, открытый, все у него идет по плану без глупостей и лишних выдумок бесхитростный, исполнительный, цельная натура. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте ESTJ. Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ISTJ':
    user_full = 'Тип Инспектор или Опекун: на первом месте - долг, человек слова, ответственный спокойный, твердый, надежный, логичный, малоэмоциональный семьянин ему свойственны обстоятельность и даже въедливость. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте  Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ISTP':
    user_full = 'Тип Мастер: субординация - излишняя условность бесстрашие, жажда действий увлечения с оттенком экстремальности умение обращаться с любыми инструментами и механизмами это боевики, наемники им свойственны братские взаимоотношения формальное образование не обязательный вариант для них (часто бросают школу и редко стремятся к высшему образованию). Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте  Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ESTP':
    user_full = 'Тип Маршал или Антрепренер: энергия, игра, неистощимый, искушенный в обращении с людьми остроумие, прагматизм работа в условиях риска и на грани катастрофы поиск острых ощущений преследуют выгоду во взаимоотношениях погоня за Госпожой Удачей, риск. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте  Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'INTP':
    user_full = 'Тип Критик или Архитектор: ценитель мыслей и языка мгновенная оценка ситуации, логичность познание законов природы интеллектуал, несколько высокомерный, интеллигент, философ, математик, теоретик, неистощимый фонтан новых идей чуткий и умный родитель отличается сложным внутренним миром богатство ассоциаций. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ENTP':
    user_full = 'Тип Искатель или Изобретатель": применяет интуицию на практике (в изобретениях), энтузиаст, новатор важна воплощенная идея, а не идея сама по себе приятный собеседник, инициативный в общении нетерпение к банальным, рутинным операциям, хороший педагог любит юмор девиз: "Понимать людей"! Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ENTJ':
    user_full = 'Тип Предприниматель или Фельдмаршал: руководитель-стратег ориентация на цель логичный эффективность в работе превыше всего хранитель домашнего очага интеллигент требовательный родитель, неутомимый карьера иногда важнее, чем семейное благополучие. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте    Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'INTJ':
    user_full = 'Тип Аналитик или Исследователь: самоуверенный его интересы в будущем авторитет положения или звания не имеет значения теоретик, приверженец "мозгового штурма", жизнь - игра на гигантской шахматной доске дефицит внешней эмоциональности, высокие способности к обучению, независимость, интуиция возможны трудности в мире эмоций и чувств. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте    Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ESFJ':
    user_full = 'Тип Энтузиаст или Торговец: открытый, практичный, расчетливый, обладает житейской мудростью компанейский, гостеприимный деловой, ответственный, интересы клиента превыше всего общительный. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ISFJ':
    user_full = 'Тип Хранитель или Консерватор: спокойный защищает интересы организации, традиции ответственный придерживается связи времен, проявляет интерес к истории все у него по плану заботливый выполнять поручения для него спокойнее, чем руководить хозяин в доме. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте    Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ISFP':
    user_full = 'Тип Посредник или Художник: успешное художественное творчество, эпикурейский образ жизни острота ощущения текущей минуты высокая чувствительность к оттенкам и полутонам в ощущениях тонкости устной и письменной речи обычно не интересуют свобода, оптимистичность, непокорность, уход от всякого рода ограничений. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ESFP':
    user_full = 'Тип Политик или Тамада: оптимизм и теплота избегают одиночества идут по жизни смеясь, жизнь для них - сплошные приключения игнорируют все мрачное щедрость, поддаются соблазнам старший друг для своего ребенка умение вдохновлять людей, приземленность языка наука - дело не для них, они выбирают бизнес, торговлю. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'INFP':
    user_full = 'Тип Лирик или Романтик: спокойный, идеалист чувство собственного достоинства борется со злом за идеалы добра и справедливости отличается лирическим символизмом это писатель, психолог, архитектор кто угодно, только не бизнесмен способности в изучении языков принцип "Мой дом - моя крепость" уживчивые и покладистые супруги. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ENFP':
    user_full = 'Тип Советчик или Журналист: умение влиять на окружающих видит людей насквозь отрывается от реальности в поиске гармонии подмечает все экстраординарное ему свойственны чувствительность, отрицание сухой логики, творчество, энтузиазм, оптимизм, богатая фантазия это торговец, политик, драматург, практический психолог ему присущи экстравагантность, щедрость, иногда избыточная. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'ENFJ':
    user_full = 'Тип Наставник или Педагог: гуманистический лидер, общительный, внимательный к чувствам других людей, образцовый родитель нетерпеливый по отношению к рутине и монотонной деятельности отличается умением распределить роли в группе. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

if user_nnnn == 'INFJ':
    user_full = 'Тип Гуманист или Предсказатель: радость друзей - радость и для него проницательность и прозорливость успешное самообразование ранимость, не любят споров и конфликтов богатое воображение, поэтичность, любовь к метафорам это психолог, врачеватель, писатель стремится к гармонии человеческих взаимоотношений. Описание полностью смотрите по адресу: ilyaklishin.ru далее перейдите в People и выбирайте   Доступ к скрытым материалам запросите у своего менеджера.'

print(user_full)
print('Помните, что темпераменты и типы - это возможности, а не способности и что существует корреляция. Когда кто-то имеет предпочтение к чему-либо, он склонен много заниматься этим и поэтому развивает свои способности в этом виде деятельности. Тогда вероятно, что предыдущий параграф верен, хотя исключения всегда найдутся. Так что NF может иметь в себе достаточно SР, чтобы быть превосходным в стратегии и лучшим в логистике, чем можно было бы ожидать (хотя логистика бы должна была быть его наименее квалифицированной ролью).')
print('Спасибо! Тестирование закончилось.')
print('Результат тестирования: ' + user_full)

with open('text.txt', 'w') as file:
    file.write(user_full)

