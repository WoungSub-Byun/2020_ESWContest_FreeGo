package com.example.myapplication

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.fragment.app.Fragment

class GuideFragment2 : Fragment() {

    private lateinit var guide2Image2 : ImageView
    private lateinit var guide2Button : ImageView
    private lateinit var guide2Text : TextView

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view =inflater.inflate(R.layout.fragment_guide2, container, false)

        guide2Image2 = view.findViewById(R.id.guide2Image2)
        guide2Button = view.findViewById(R.id.guide2Button)
        guide2Text = view.findViewById(R.id.guide2Text)

        guide2Image2.animate().alpha(1f).setDuration(1000).start()
        guide2Button.animate().alpha(1f).setDuration(1000).withEndAction {
            guide2Text.animate().alpha(1f).setDuration(1000).start()
        }.start()

        return view
    }


}