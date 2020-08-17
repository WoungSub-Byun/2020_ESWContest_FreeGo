package com.example.myapplication.retrofit.DTO

import java.util.*

data class User(
    val name : String
)

data class FridgeDTO(
    val productName : String,
    val productNumber : Int,
    val data : Date,
    val userName : String
)