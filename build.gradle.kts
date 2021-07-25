import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

val groovyVersion: String by project
val hopliteVersion: String by project
val kordexVersion: String by project
val kotlinLoggingVersion: String by project
val logbackVersion: String by project
val tnoodleVersion: String by project

plugins {
    kotlin("jvm") version "1.5.20"
}

group = "com.mcuberzz"
version = "1.0.0"

repositories {
    mavenCentral()
    maven {
        name = "Kotlin Discord"
        url = uri("https://maven.kotlindiscord.com/repository/maven-public/")
    }
}

dependencies {
    implementation("ch.qos.logback:logback-classic:$logbackVersion")
    implementation("com.kotlindiscord.kord.extensions:kord-extensions:$kordexVersion")
    implementation("io.github.microutils:kotlin-logging:$kotlinLoggingVersion")
    implementation("org.codehaus.groovy:groovy:$groovyVersion")
    implementation("org.worldcubeassociation.tnoodle:lib-scrambles:$tnoodleVersion")
}

tasks.withType<KotlinCompile>() {
    kotlinOptions {
        jvmTarget = "11"
        freeCompilerArgs = freeCompilerArgs + "-Xopt-in=kotlin.RequiresOptIn"
    }
}
