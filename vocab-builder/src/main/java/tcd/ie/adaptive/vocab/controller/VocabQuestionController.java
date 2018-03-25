package tcd.ie.adaptive.vocab.controller;

import java.io.File;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import edu.mit.jwi.Dictionary;
import edu.mit.jwi.IDictionary;
import edu.mit.jwi.item.IIndexWord;
import edu.mit.jwi.item.ISynset;
import edu.mit.jwi.item.IWord;
import edu.mit.jwi.item.IWordID;
import edu.mit.jwi.item.POS;
import edu.mit.jwi.item.Pointer;
import tcd.ie.adaptive.vocab.entity.VocabQuesResponse;

@Controller
@EnableAutoConfiguration
@PropertySource({"classpath:application.properties"})
@RequestMapping({"/vocab/"})
public class VocabQuestionController {
		
	@Autowired
	private Environment environment;
	
	private IDictionary getDictionary;
	
	public void loadWordNet() {
		try {
			File file = new ClassPathResource(environment.getProperty("wordnet.path")).getFile();			
			String path = file.getAbsolutePath() + File.separator + "dict" ;
			URL url = new URL ( "file" , null , path ) ;
			this.getDictionary = new Dictionary(url) ;
			getDictionary.open();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
		
	@RequestMapping(value={"/{word}"}, method={RequestMethod.GET}, produces={"application/json"})
	@ResponseBody
	public String getVocabularyQuestionByWord(@PathVariable String word) {
		loadWordNet();
		
		VocabQuesResponse vocabQuesResp = new VocabQuesResponse(); 
		
		vocabQuesResp.setWord(word);
		IIndexWord idxWord = getDictionary.getIndexWord(word, POS.ADJECTIVE) ;
		IWordID wordID = idxWord.getWordIDs().get(0) ;
		IWord getWord = getDictionary.getWord(wordID) ;
		List<IWordID> wordIds = getWord.getRelatedWords(Pointer.ANTONYM);
		List<String> anatonym = new ArrayList<>();;
		for (IWordID iWordID : wordIds) {
			anatonym.add(getDictionary.getWord(iWordID).getLemma());
		}
		vocabQuesResp.setAntonym(anatonym);
		
		ISynset synset = getWord.getSynset();
		List<IWord> synsetWords = synset.getWords();
		List<String> synonym = new ArrayList<>();
		for (IWord iWord : synsetWords) {
			synonym.add(iWord.getLemma());
		}
		vocabQuesResp.setSynonym(synonym);
		vocabQuesResp.setGloss(synset.getGloss());
		ObjectMapper mapper = new ObjectMapper();
		String response = null;
		try {
			response = mapper.writeValueAsString(vocabQuesResp);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return response;
		
	}
}
