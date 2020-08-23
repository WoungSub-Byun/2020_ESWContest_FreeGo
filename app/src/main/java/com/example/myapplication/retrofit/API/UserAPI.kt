package com.example.myapplication.retrofit.API

import com.example.myapplication.retrofit.DTO.FirstData
import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface UserAPI {
    @POST("/register")
    fun register(
        @Field("id") id : String,
        @Field("pwd") pwd : String
    ) : Call<FirstData>

    @GET("/finduser/{id}")
    fun getUser(
        @Path("id") id: String
    ) : Call<FirstData>
    @POST("/login")
    fun login(
        @Field("id") id: String,
        @Field("pwd") pwd: String
    ) : Call<FirstData>
}