package com.example.myapplication.retrofit.API

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.create

class RetrofitHelper {

    val retrofit: Retrofit = Retrofit.Builder()
        .baseUrl("")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getFridgeAPI() : FridgeAPI{
        return retrofit.create(FridgeAPI::class.java)
    }
    fun getUserAPI() : UserAPI{
        return retrofit.create(UserAPI::class.java)
    }
}