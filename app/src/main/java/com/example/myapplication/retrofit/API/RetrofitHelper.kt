package com.example.myapplication.retrofit.API

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.create

class RetrofitHelper {
    fun getRetrofit() : FridgeAPI{
        return Retrofit.Builder()
            .baseUrl("")
            .addConverterFactory(GsonConverterFactory.create())
            .build().create(FridgeAPI::class.java)
    }
}