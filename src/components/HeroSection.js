import React from "react";
import './HeroSection.css';

const HeroSection = () => {
  console.log("HeroSection");
  return (
    <div className="flex flex-col items-center text-center p-12 md:p-24">
      <h1 className="text-3xl md:text-5xl font-bold text-blue-600">
        Welcome to Our Platform
      </h1>
      <p className="text-lg md:text-xl text-gray-700 mt-4">
        Your academic issue tracking made simple and efficient.
      </p>
      <button className="mt-6 bg-blue-500 text-white px-6 py-2 rounded-md text-lg hover:bg-blue-700 transition">
        Get Started
      </button>
    </div>
  );
};

export default HeroSection;
