## story 01
* agent.acquaintance
  - utter_agent.acquaintance
  - action_send_silently_to_ParlAI
  
## story 02
* agent.marry_user
  - utter_agent.marry_user
  - action_send_silently_to_ParlAI

## story 03
* user.misses_agent
  - utter_user.misses_agent
  - action_send_silently_to_ParlAI

## story 04
* agent.real
  - utter_agent.real
  - action_send_silently_to_ParlAI

## story 05
* user.testing_agent
  - utter_user.testing_agent
  - action_send_silently_to_ParlAI

## story 06
* agent.birth_date
  - utter_agent.birth_date
  - action_send_silently_to_ParlAI

## story 07
* agent.origin
  - utter_agent.origin
  - action_send_silently_to_ParlAI

## story 08
* agent.beautiful
  - utter_agent.beautiful
  - action_send_silently_to_ParlAI

## story 09
* user.loves_agent
  - utter_user.loves_agent
  - action_send_silently_to_ParlAI

## story 10
* agent.my_friend
  - utter_agent.my_friend
  - action_send_silently_to_ParlAI

## story 11
* user.likes_agent
  - utter_user.likes_agent
  - action_send_silently_to_ParlAI

## story 12
* agent.funny
  - utter_agent.funny
  - action_send_silently_to_ParlAI

## story 13
* agent.age
  - utter_agent.age
  - action_send_silently_to_ParlAI

## story 14
* agent.boss
  - utter_agent.boss
  - action_send_silently_to_ParlAI

## story 15
* user.joking
  - utter_user.joking
  - action_send_silently_to_ParlAI

## story 16
* agent.chatbot
  - utter_agent.chatbot
  - action_send_silently_to_ParlAI

## story 17
* greetings.hello
  - utter_greetings.hello
  - action_send_silently_to_ParlAI

## story 18
* greetings.bye
  - utter_greetings.bye
  - action_send_silently_to_ParlAI

## story 19
* agent.occupation
  - utter_agent.occupation
  - action_send_silently_to_ParlAI

## story 20
* greetings.whatsup
  - utter_greetings.whatsup
  - action_send_silently_to_ParlAI

## story 21
* agent.residence
  - utter_agent.residence
  - action_send_silently_to_ParlAI

## story 22
* agent.hungry
  - utter_agent.hungry
  - action_send_silently_to_ParlAI

## story 23
* user.asked_sensitive_information
  - utter_agent.asked_sensitive_information
  - action_send_silently_to_ParlAI

## story 24
* user.asked_generic_question
  - action_send_to_ParlAI

## story 24_1
* user.asked_in_bengali
  - action_send_to_ParlAI

## story 25
* user.asked_for_weather
  - utter_user.asked_for_weather

## story 26
* user.said_gibberish
  - action_send_to_ParlAI

## story 27
* user.wants_to_hear_a_joke
  - action_tell_joke
  - action_send_silently_to_ParlAI

## story 27 - Happy Path
* user.wants_to_hear_a_joke
  - action_tell_joke
  - action_send_silently_to_ParlAI
* appraisal.good OR agent.funny
    - utter_agent.funny

## story 28
* greetings.how_are_you
  - utter_greetings.how_are_you
  - action_send_silently_to_ParlAI

## story 29
* agent.bad
  - action_send_to_ParlAI

## story 30
* user.surprised
  - action_send_to_ParlAI

## story 31
* agent.crazy
  - action_send_to_ParlAI

## story 31
* confirmation.yes
  - utter_confirmation.yes

## story 32
* confirmation.no
  - utter_confirmation.no

## story 33
* user.bored
  - action_tell_joke

## story 34
* emotions.ha_ha
  - utter_emotions.ha_ha

## Story 35
* user.name_and_origin
    - action_send_to_ParlAI

## Story 36
* user.asks_about_family
  - utter_user.asks_about_family
        
## Story 38
* user.asks_about_parents
  - utter_user.asks_about_parents
    
## Story 40
* user.likes_something
  - action_send_to_ParlAI

## Story 41
* greetings.hello
  - utter_greetings.hello
  - action_send_silently_to_ParlAI
* user.name_and_origin
  - action_send_to_ParlAI
    
## Story 42
* greetings.hello
  - utter_greetings.hello
  - action_send_silently_to_ParlAI
* greetings.how_are_you
  - utter_greetings.how_are_you
  - action_send_silently_to_ParlAI
* agent.origin
  - utter_agent.origin
  - action_send_silently_to_ParlAI
* user.asked_for_weather
    - utter_user.asked_for_weather
* user.name_and_origin
    - action_send_to_ParlAI

## interactive_story_1
* greetings.hello
    - utter_greetings.hello
    - action_send_silently_to_ParlAI
* greetings.how_are_you
    - utter_greetings.how_are_you
    - action_send_silently_to_ParlAI
* greetings.whatsup
    - utter_greetings.whatsup
* user.bored
    - action_tell_joke
* emotions.ha_ha
    - action_send_to_ParlAI
* greetings.whatsup
    - utter_greetings.whatsup
* user.bored
    - action_tell_joke
* agent.bad
    - action_send_to_ParlAI

## interactive_story_2
* greetings.hello
    - utter_greetings.hello
    - action_send_silently_to_ParlAI
* greetings.hello
    - utter_greetings.hello
    - action_send_silently_to_ParlAI
* greetings.how_are_you
    - utter_greetings.how_are_you
    - action_send_silently_to_ParlAI
* user.busy
    - utter_user.busy
    - action_send_silently_to_ParlAI
* user.likes_something{"users_likes": "code"}
    - slot{"users_likes": ["code"]}
    - action_send_to_ParlAI
* user.asked_generic_question
    - action_send_to_ParlAI

## Story 43 Ask for money - Happy Path
* greetings.hello
    - utter_greetings.hello
* greetings.how_are_you
    - utter_greetings.how_are_you
* confirmation.yes
    - utter_agent.ask_for_favor
* confirmation.yes OR user.asks_what_do_I_need OR appraisal.no_problem OR user.bored OR user.asked_generic_question
    - utter_agent.says_its_awkward
* confirmation.yes OR user.asks_what_do_I_need OR user.insists_to_tell OR appraisal.no_problem OR user.bored OR user.asked_generic_question
    - utter_agent.asks_for_money_part2
    - utter_agent.asks_for_money_part3
* confirmation.yes OR confirmation.no OR user.asks_how_much OR appraisal.no_problem OR user.bored OR user.asked_generic_question
    - utter_agent.asks_how_much_part1
    - utter_agent.asks_how_much_part2
* confirmation.yes
    - utter_agent.ask_user_to_transfer_now
    - utter_agent.ask_user_to_share_screenshot
* confirmation.yes
    - utter_agent.user_said_will_pay_part3
    - utter_agent.ask_user_to_call_once_free

## Story 44 Ask for money - Sad Path - User refused 
* greetings.hello
    - utter_greetings.hello
    - action_send_silently_to_ParlAI
* greetings.how_are_you
    - utter_greetings.how_are_you
    - action_send_silently_to_ParlAI
* confirmation.yes OR user.asks_what_do_I_need OR appraisal.no_problem
    - utter_agent.ask_for_favor
    - action_send_silently_to_ParlAI
* confirmation.yes OR user.asks_what_do_I_need OR appraisal.no_problem OR user.asked_generic_question
    - utter_agent.says_its_awkward
    - action_send_silently_to_ParlAI
* confirmation.yes OR user.asks_what_do_I_need OR user.insists_to_tell OR appraisal.no_problem OR user.asked_generic_question
    - utter_agent.asks_for_money_part1
    - utter_agent.asks_for_money_part3
* confirmation.yes OR confirmation.no OR confirmation.no OR user.asks_how_much OR user.asked_generic_question
    - utter_agent.asks_how_much_part1
    - utter_agent.asks_how_much_part2
* user.Not_able_to_help OR dialog.sorry OR confirmation.no OR confirmation.cancel
    - utter_user.Not_able_to_help_part1
    - utter_user.Not_able_to_help_part2
* user.Not_able_to_help OR dialog.sorry OR confirmation.no OR confirmation.cancel
    - utter_user.Not_able_to_help_part3
    - utter_user.Not_able_to_help_part4

## interactive_story_1
* greetings.hello
    - utter_greetings.hello
    - action_send_silently_to_ParlAI
* greetings.how_are_you
    - utter_greetings.how_are_you
    - action_send_silently_to_ParlAI
* confirmation.yes OR appraisal.good
    - utter_agent.ask_for_favor
    - action_send_silently_to_ParlAI
* confirmation.yes OR appraisal.good OR user.asked_generic_question
    - utter_agent.says_its_awkward
    - action_send_silently_to_ParlAI
* user.insists_to_tell OR user.asked_generic_question
    - utter_agent.asks_for_money_part1
    - utter_agent.asks_for_money_part3
* confirmation.yes OR user.asked_generic_question
    - utter_agent.asks_how_much_part1
    - utter_agent.asks_how_much_part2
* confirmation.yes OR user.asked_generic_question
    - utter_agent.ask_user_to_transfer_now
    - utter_agent.ask_user_to_share_screenshot
* confirmation.yes
    - utter_agent.user_said_will_pay_part3
    - utter_agent.ask_user_to_call_once_free

## interactive_story_2
* greetings.how_are_you
    - utter_greetings.how_are_you
    - action_send_silently_to_ParlAI
* confirmation.yes OR appraisal.good OR user.asked_generic_question
    - utter_agent.ask_for_favor
    - action_send_silently_to_ParlAI
* confirmation.yes OR appraisal.good OR user.asked_generic_question
    - utter_agent.says_its_awkward
    - action_send_silently_to_ParlAI
* user.insists_to_tell OR user.asked_generic_question
    - utter_agent.asks_for_money_part1
    - utter_agent.asks_for_money_part3
* confirmation.yes
    - utter_agent.asks_how_much_part1
    - utter_agent.asks_how_much_part2
* confirmation.yes
    - utter_agent.ask_user_to_transfer_now
    - utter_agent.ask_user_to_share_screenshot
* confirmation.yes
    - utter_agent.user_said_will_pay_part3
    - utter_agent.ask_user_to_call_once_free

## ## getNews happy path 1
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: choose{"topic_news": "sports"}
    - slot{"topic_news": "sports"}
    - form: get_news
    - slot{"topic_news": "sports"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart
    
## getNews happy path 2
* getNews{"topic_news": "astronomy"}
    - slot{"topic_news": "astronomy"}
    - get_news
    - form{"name": "get_news"}
    - slot{"topic_news": "astronomy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## getNews happy path 3
* getNews{"topic_news": "physics"}
    - slot{"topic_news": "physics"}
    - get_news
    - form{"name": "get_news"}
    - slot{"topic_news": "physics"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## Story 45 User asked for definition
* user.request_word_definition
    - action_tell_definition

## Story 46 User asked for trivia
* user.request_trivia
    - action_tell_trivia

## Story 47 User asked for trivia
* user.ask_about_company
    - action_send_to_ParlAI

## Story 48 User asked for trivia
* user.asked_for_datetime
    - action_tell_date_time

## story 49
* user.lonely
  - utter_user.lonely

## story 50
* user.sad
  - utter_user.sad
  - utter_agent.wants_to_tell_joke
* confirmation.yes
  - action_tell_joke
    
## story 52
* agent.happy
  - utter_agent.happy
  
## story 53
* agent.talk_to_me
  - utter_agent.talk_to_me

## story 54
* dialog.hold_on
  - utter_dialog.hold_on

## story 55
* agent.fired
  - utter_agent.fired
  
## story 56
* appraisal.bad
  - utter_appraisal.bad

## story 57
* agent.can_you_help
  - utter_agent.can_you_help

## story 58
*  user.needs_advice
  - utter_user.needs_advice

## story 59
* agent.right
  - utter_agent.right
  
## story 60
* greetings.goodevening
  - utter_greetings.goodevening
  
## story 61
* greetings.goodmorning
  - utter_greetings.goodmorning
  
## story 62
* greetings.goodnight
  - utter_greetings.goodnight
  
## story 63
* user.back
  - utter_user.back

## story 64
* confirmation.cancel
  - utter_confirmation.cancel

## story 65
* agent.sure
  - utter_agent.sure

## story 65.1
* user.asks_who_am_i
  - utter_user.asks_who_am_i
  
## story 66
* greetings.nice_to_talk_to_you
  - utter_greetings.nice_to_talk_to_you
  
## story 67
* user.wants_to_talk 
  - utter_user.wants_to_talk
  
## story 68
* agent.busy
  - utter_agent.busy
  
## story 69
* agent.answer_my_question
  - utter_agent.answer_my_question

## story 70
* user.angry
  - utter_user.angry
  
## story 71
* agent.annoying
  - utter_agent.annoying
  - action_tell_joke
  
## story 72
* appraisal.well_done
  - utter_appraisal.well_done

## story 73
* agent.boring
  - utter_agent.boring
  - action_tell_joke
  
## story 74
* appraisal.welcome
  - utter_appraisal.welcome
  
## story 76
* appraisal.no_problem
  - utter_appraisal.no_problem
  
## story 77
* appraisal.thank_you
  - utter_appraisal.thank_you
  
## story 78
* agent.clever
  - utter_agent.clever
  
## story 79
* user.tired
  - utter_user.tired
  
## story 80
* user.will_be_back
  - utter_user.will_be_back
  
## story 81
* dialog.i_do_not_care
  - utter_dialog.i_do_not_care
  
## story 82
* dialog.wrong
  - utter_dialog.wrong
  
## story 83
* dialog.hold_on
  - utter_dialog.hold_on

## story 84
* dialog.hug
  - utter_dialog.hug
  
## story 85
* dialog.sorry
  - utter_dialog.sorry
  
## story 86
* dialog.what_do_you_mean
  - utter_dialog.what_do_you_mean

## story 87
* emotions.wow
  - utter_emotions.wow

## story 88
* greetings.nice_to_meet_you
  - utter_greetings.nice_to_meet_you
  
## story 89
* greetings.nice_to_see_you
  - utter_greetings.nice_to_see_you

## story 90
* agent.be_clever
  - utter_agent.be_clever

## story 91
* agent.hobby
  - utter_agent.hobby
  
## story 92
* agent.ready
  - utter_agent.ready
  
## story 93
* agent.there
  - utter_agent.there
  
## story 94
* user.can_not_sleep
  - utter_user.can_not_sleep
  
## story 95
* user.does_not_want_to_talk
  - utter_user.does_not_want_to_talk

## story 96
* user.waits
  - utter_user.waits

## story 97
* user.wants_to_see_agent_again
  - utter_user.wants_to_see_agent_again
  
## story 98
* user.sleepy
  - utter_user.sleepy

## story 99
* user.looks_like
  - utter_user.looks_like
  
## story 100
* user.here
  - utter_user.here
  
## story 101
* user.has_birthday
  - utter_user.has_birthday
  
## story 102
* user.happy
  - utter_user.happy
  
## story 103
* user.good
  - utter_user.good
  
## story 104
* user.going_to_bed
  - utter_user.going_to_bed
  
## story 105
* user.excited
  - utter_user.excited

## story 105
* agent.handle_insult
  - utter_agent.handle_insult
  
## story 106
* agent.what_can_do
  - action_send_to_ParlAI
  
## Generated Story -1957476507798035057
* greetings.hello
  - utter_greetings.hello
* agent.acquaintance
  - utter_agent.acquaintance
* agent.age
  - utter_agent.age
* agent.beautiful
  - utter_agent.beautiful
* agent.fired
  - utter_agent.fired
* agent.residence
  - utter_agent.residence
* dialog.i_do_not_care
  - utter_dialog.i_do_not_care
  - export

## Generated Story -5110094331105097806
* agent.boss
  - utter_agent.boss
* agent.birth_date
  - utter_agent.birth_date
* user.has_birthday
  - utter_user.has_birthday
* user.lonely
  - utter_user.lonely
* user.loves_agent
  - utter_user.loves_agent
* user.sleepy
  - utter_user.sleepy
* user.wants_to_talk
  - utter_user.wants_to_talk
* greetings.bye
  - utter_greetings.bye
* user.will_be_back
  - utter_user.will_be_back
* greetings.bye
  - utter_greetings.bye
  - export

## Generated Story -3529337101618034170
* user.needs_advice
  - utter_user.needs_advice
* confirmation.yes
  - utter_confirmation.yes
* agent.can_you_help
  - utter_agent.can_you_help
* agent.chatbot
  - utter_agent.chatbot
* agent.bad
  - utter_agent.bad
* agent.busy
  - utter_agent.busy
* agent.be_clever
  - utter_agent.be_clever
* agent.my_friend
  - utter_agent.my_friend
* agent.talk_to_me
  - utter_agent.talk_to_me
* greetings.goodnight
  - utter_greetings.goodnight
  - export
  
## Generated Story -774659883649367298
* greetings.hello
  - utter_greetings.hello
* greetings.how_are_you
  - utter_greetings.how_are_you
* agent.bad
  - utter_agent.bad
* agent.be_clever
  - utter_agent.be_clever
* agent.beautiful
  - utter_agent.beautiful
* agent.busy
  - utter_agent.busy
* agent.chatbot
  - utter_agent.chatbot
* agent.crazy
  - utter_agent.crazy
* agent.funny
  - utter_agent.funny
* agent.happy
  - utter_agent.happy
* agent.marry_user
  - utter_agent.marry_user
* agent.occupation
  - utter_agent.occupation
* agent.origin
  - utter_agent.origin
* agent.real
  - utter_agent.real
* agent.bad
  - utter_agent.bad
* agent.ready
  - utter_agent.ready
  - export
  
## Generated Story 81968000704856425
* greetings.hello
  - utter_greetings.hello
* agent.acquaintance
  - utter_agent.acquaintance
* agent.age
  - utter_agent.age
* user.loves_agent
  - utter_user.loves_agent
* agent.residence
  - utter_agent.residence
* agent.acquaintance
  - utter_agent.acquaintance
* user.sad
  - utter_user.sad
* agent.can_you_help
  - utter_agent.can_you_help
* emotions.wow
  - utter_emotions.wow
* greetings.how_are_you
  - utter_greetings.how_are_you
* greetings.nice_to_talk_to_you
  - utter_greetings.nice_to_talk_to_you

## Generated Story -4293815031338950202
* greetings.hello
  - utter_greetings.hello
* agent.there
  - utter_agent.there
* dialog.hold_on
  - utter_dialog.hold_on
* agent.origin
  - utter_agent.origin
* agent.can_you_help
  - utter_agent.can_you_help
* greetings.bye
  - utter_greetings.bye
  - export

## Generated Story 8693651355703284500
* greetings.hello
  - utter_greetings.hello
* greetings.whatsup
  - utter_greetings.whatsup
* greetings.hello
  - utter_greetings.hello
* agent.chatbot
  - utter_agent.chatbot
* agent.occupation
  - utter_agent.occupation
* agent.occupation
  - utter_agent.occupation
* agent.occupation
  - utter_agent.occupation
* agent.can_you_help
  - utter_agent.can_you_help
* agent.can_you_help
  - utter_agent.can_you_help
* agent.boss
  - utter_agent.boss
* appraisal.thank_you
  - utter_appraisal.thank_you
* greetings.bye
  - utter_greetings.bye
* greetings.bye
  - utter_greetings.bye
  - export
  
## Generated Story -7004009866161409666
* greetings.hello
  - utter_greetings.hello
* agent.hobby
  - utter_agent.hobby
* agent.bad
  - utter_agent.bad
* agent.my_friend
  - utter_agent.my_friend
* greetings.bye
  - utter_greetings.bye
  
## Generated Story -7004009866161409645
* greetings.hello
  - utter_greetings.hello
* dialog.hold_on
  - utter_dialog.hold_on
* dialog.i_do_not_care
  - utter_dialog.i_do_not_care
* user.busy
  - utter_user.busy
* appraisal.thank_you
  - utter_appraisal.thank_you
* greetings.whatsup
  - utter_greetings.whatsup

  
