package com.example.simplecurrencyapi.repository;

import com.example.simplecurrencyapi.model.Currency;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import java.util.Optional;

@Tag(name = "Взаимодействие с курсом валют")
@RepositoryRestResource(collectionResourceRel = "currencies", path = "currencies")
public interface CurrencyRepository extends JpaRepository<Currency, Long> {

    @Operation(summary = "Получение курса по имени валюты")
    Optional<Currency> findByNameIgnoreCase(@Param("name") String name);
}
