package com.example.simplecurrencyapi.model;

import jakarta.persistence.*;
import lombok.Data;
import org.hibernate.annotations.GenericGenerator;
import org.hibernate.annotations.Parameter;

@Data
@Entity
@Table(name = "currency")
public class Currency {

    @Id
    @GenericGenerator(
            name = "currency_gen",
            parameters = {
                    @Parameter(name = "sequence_name", value = "currency_id_seq"),
                    @Parameter(name = "optimizer", value = "pooled-lo"),
                    @Parameter(name = "initial_value", value = "1"),
                    @Parameter(name = "increment_size", value = "1")
            }
    )
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "currency_gen")
    private Long id;
    private String name;
    private Double rate;

}
