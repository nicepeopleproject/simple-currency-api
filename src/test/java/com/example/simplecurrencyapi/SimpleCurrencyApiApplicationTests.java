package com.example.simplecurrencyapi;

import com.example.simplecurrencyapi.model.Currency;
import com.example.simplecurrencyapi.repository.CurrencyRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.hateoas.MediaTypes.HAL_JSON_VALUE;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@SpringBootTest(classes = SimpleCurrencyApiApplication.class)
@AutoConfigureMockMvc
class SimpleCurrencyApiApplicationTests {

    private static final String USD = "USD";
    private static final Double USD_RATE = 90.5;

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private CurrencyRepository currencyRepository;

    @Test
    public void testFindCurrencyByName() throws Exception {
        Currency currency = new Currency();
        currency.setName(USD);
        currency.setRate(USD_RATE);

        currency = currencyRepository.save(currency);

        mockMvc.perform(get("/currencies/search/findByNameIgnoreCase")
                        .param("name", "usd")
                        .contentType(HAL_JSON_VALUE))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value(currency.getName()))
                .andExpect(jsonPath("$.rate").value(currency.getRate()));
    }

}
