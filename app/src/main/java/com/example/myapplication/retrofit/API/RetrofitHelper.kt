package com.example.myapplication.retrofit.API

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class RetrofitHelper {

    val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl("http://13.125.244.112:5000")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getFridgeAPI() : FridgeAPI{
        return retrofit.create(FridgeAPI::class.java)
    }
    fun getUserAPI() : UserAPI{
        return retrofit.create(UserAPI::class.java)
    }
}