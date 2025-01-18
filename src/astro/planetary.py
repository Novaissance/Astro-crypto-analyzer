import ephem
from datetime import datetime

class PlanetaryCalculator:
    def __init__(self):
        self.observer = ephem.Observer()
        self.planets = {
            'sun': ephem.Sun(),
            'moon': ephem.Moon(),
            'mars': ephem.Mars(),
            'venus': ephem.Venus(),
            'jupiter': ephem.Jupiter(),
            'saturn': ephem.Saturn()
        }
    
    def get_position(self, planet_name, date=None):
        """Calculate planetary position for given date"""
        if date is None:
            date = datetime.utcnow()
        
        self.observer.date = date
        planet = self.planets[planet_name.lower()]
        planet.compute(self.observer)
        
        return {
            'ra': float(planet.ra) * 180/ephem.pi,
            'dec': float(planet.dec) * 180/ephem.pi,
            'phase': getattr(planet, 'phase', None)
        }

    def get_aspects(self, planet1, planet2, date=None):
        """Calculate aspects between two planets"""
        pos1 = self.get_position(planet1, date)
        pos2 = self.get_position(planet2, date)
        
        # Calculate angular separation
        separation = abs(pos1['ra'] - pos2['ra'])
        
        # Define aspect types
        aspects = {
            0: 'conjunction',
            60: 'sextile',
            90: 'square',
            120: 'trine',
            180: 'opposition'
        }
        
        # Check for aspects with 5 degree orb
        for angle, aspect in aspects.items():
            if abs(separation - angle) <= 5:
                return aspect
        
        return None