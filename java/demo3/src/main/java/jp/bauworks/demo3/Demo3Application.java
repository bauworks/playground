package jp.bauworks.demo3;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import jp.bauworks.demo3.service.*;

@SpringBootApplication
public class Demo3Application {

	public static void main(String[] args) {
		//SpringApplication.run(Demo3Application.class, args);

        ConfigurableApplicationContext ctx = SpringApplication.run(Demo3Application.class, args);
        SampleService service = ctx.getBean(SampleService.class);
        System.out.println(service.execute());

	}

}
