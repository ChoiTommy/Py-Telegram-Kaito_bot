package main
import (
	"github.com/go-telegram-bot-api/telegram-bot-api"
  "io/ioutil"
	"log"
  "math/rand"
  "time"
)
func main(){
  bot, err := tgbotapi.NewBotAPI(getKey("key.txt"))
	if err != nil {
		log.Panic(err)
	}
  rand.Seed(time.Now().UnixNano())
	bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)

  k := 434;
  /*u := tgbotapi.NewUpdate(0)
	u.Timeout = 60
  updates, err := bot.GetUpdatesChan(u)*/

  channelid := int64(-1001321795482);
  chatid := int64(-1001356677647); //-1001356677647 timChunw 407572346


  for {
    msg := tgbotapi.NewForward(chatid, channelid, getRand(k))
    m, err := bot.Send(msg)
    _ = m
    for err != nil {
  		log.Printf("error: ", err)
      m, err = bot.Send(tgbotapi.NewForward(chatid, channelid, getRand(k)))
      _ = m
  	}
    //bot.Send(tgbotapi.NewMessage(chatid, ""))
    time.Sleep(2*time.Hour)
  }


  /*for update := range updates {
		if update.Message.Chat.IsChannel() == true {
			k++
      log.Printf("k value: ", k)
		}
  }*/
}

func getRand(k int) int{
  return rand.Intn(k - 297 + 1) + 297
}

func getKey(path string) string {
		key, err := ioutil.ReadFile(path)
		if err != nil {
			log.Panicf("failed reading data from file: %s", err)
		}
		return string(key)
}
