"""
@file geometry.py
@brief This module provides basic geometric operations.
"""

class Geometry:
    """!
    @brief Geometry class for basic geometric operations.
    """

## @defgroup RectangleGroup Rectangle
## @brief Group for all rectangle-related functions.
## @{
    def rectangle_area(length, width):
        """!
        Calculate the area with length and width.
        
        @param length Length of the rectangle
        @param width Width of the rectangle
        @return The area of the rectangle
        """
        return length * width

        
    def rectangle_perimeter(length, width):
        """!
        Calculate the perimeter with length and width.
        
        @param length Length of the rectangle
        @param width Width of the rectangle
        @return The perimeter of the rectangle
        """
        return (length + width) * 2
## @}
   
## @defgroup CircleGroup Circle
## @brief Group for all circle-related functions.
## @{   
    def circle_area(radius):
        """!
        Calculate the area of a circle with his radius.
        
        @param radius Radius of the circle
        @return The area of a circle
        """
        return round(3.14 * radius * radius, 2)
        
    def circle_circumference(radius):
        """!
        Calculate the circumference of a circle with his radius.
        
        @param radius Radius of the circle
        @return The circumference of a circle
        """
        return round(2 * 3.14 * radius, 2)
## @}