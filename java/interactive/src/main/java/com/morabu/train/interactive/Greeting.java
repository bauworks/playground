package com.morabu.train.interactive;

import lombok.Data;
import lombok.Getter;

@Data
public class Greeting {

	@Getter
	private String content;

	public Greeting(String content) {
		this.content = content;
	}

}
