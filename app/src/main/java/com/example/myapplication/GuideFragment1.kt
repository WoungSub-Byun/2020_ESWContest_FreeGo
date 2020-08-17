package com.example.myapplication

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.fragment.app.Fragment

class GuideFragment1 : Fragment() {

    private lateinit var guide1Image1 : ImageView
    private lateinit var guide1Button : ImageView
    private lateinit var guide1Text : TextView

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        val view = inflater.inflate(R.layout.fragment_guide1, container, false)

        guide1Image1 = view.findViewById(R.id.guide1Image1)
        guide1Button = view.findViewById(R.id.guide1Button)
        guide1Text = view.findViewById(R.id.guide1Text)

        guide1Image1.animate().alpha(1f).setDuration(1000).start()
        guide1Button.animate().alpha(1f).setDuration(1000).withEndAction{
            guide1Text.animate().alpha(1f).setDuration(1000).start()
        }.start()


        return view
    }

}