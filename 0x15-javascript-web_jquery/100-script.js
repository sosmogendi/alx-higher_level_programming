/* This script updates the text color of the <header> element to red (#FF0000)
   using document.querySelector. */

document.addEventListener("DOMContentLoaded", function () {
  // Wait for the DOM to be fully loaded before accessing elements

  // Select the <header> element
  const headerElement = document.querySelector("header");

  // Check if the element was found
  if (headerElement) {
    // Modify the text color to red
    headerElement.style.color = "#FF0000";
  }
});
