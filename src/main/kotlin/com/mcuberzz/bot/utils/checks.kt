package com.mcuberzz.bot.utils

import com.kotlindiscord.kord.extensions.checks.CheckFun
import com.kotlindiscord.kord.extensions.checks.memberFor
import com.mcuberzz.bot.admins
import dev.kord.core.event.Event

fun isAdmin(): CheckFun {
    suspend fun inner(event: Event): Boolean {
        return memberFor(event)?.id in admins
    }

    return ::inner
}
