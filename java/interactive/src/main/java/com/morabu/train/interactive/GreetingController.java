package com.morabu.train.interactive;

import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;
import org.springframework.web.util.HtmlUtils;

@Controller
public class GreetingController {


  @MessageMapping("/hello")
  @SendTo("/topic/greetings")
  public Greeting greeting(HelloMessage message) throws Exception {
	System.out.println("Hello, " + HtmlUtils.htmlEscape(message.getName()) + "!");
    Thread.sleep(1000); // simulated delay
    return new Greeting("Hello, " + HtmlUtils.htmlEscape(message.getName()) + "!");
  }

	@MessageMapping("/hello1")
	@SendTo("/topic/greetings1")
	public Greeting greeting1(HelloMessage message) throws Exception {
	  System.out.println("Hello1, " + HtmlUtils.htmlEscape(message.getName()) + "!");
	  Thread.sleep(1000); // simulated delay
	  return new Greeting("Hello1, " + HtmlUtils.htmlEscape(message.getName()) + "!");
	}

}
