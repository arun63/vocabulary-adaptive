package tcd.ie.adaptive.vocab.entity;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class VocabQuesResponse {
	
	private String word;
	private List<String> antonym;
	private List<String> synonym;
	private String gloss;
	
	public String getWord() {
		return word;
	}
	public void setWord(String word) {
		this.word = word;
	}
	public List<String> getAntonym() {
		return antonym;
	}
	public void setAntonym(List<String> antonym) {
		this.antonym = antonym;
	}
	public List<String> getSynonym() {
		return synonym;
	}
	public void setSynonym(List<String> synonym) {
		this.synonym = synonym;
	}
	public String getGloss() {
		return gloss;
	}
	public void setGloss(String gloss) {
		this.gloss = gloss;
	}
	
}
