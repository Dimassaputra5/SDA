
import time
import numpy as np
import math as mt
from typing import Callable, Dict, Tuple


class BigOAnalyzer:
    """Analyzer untuk menghitung Big O complexity dari sebuah function secara empiris.
    Support function dengan single atau multiple parameters.
    """
    
    def __init__(self, min_n=100, max_n=5000, multiplier=2, repeats=3):
        self.min_n = min_n
        self.max_n = max_n
        self.multiplier = multiplier
        self.repeats = repeats
        self.measurements = None
        self.n_values = None
        self.time_values = None
    
    def collect_data(self, func: Callable, data_gen: Callable, 
                     use_args: bool = False) -> np.ndarray:
        """Kumpulkan runtime data untuk berbagai ukuran input."""
        measurements = []
        n = self.min_n
        
        while n <= self.max_n:
            times = []
            for _ in range(self.repeats):
                if use_args:
                    args = data_gen(int(n))
                    t = self._measure_time_with_args(func, args)
                else:
                    data = data_gen(int(n))
                    t = self._measure_time(func, data)
                times.append(t)
            
            avg_time = np.mean(times)
            measurements.append((n, avg_time))
            n *= self.multiplier
        
        self.measurements = np.array(measurements)
        self.n_values = self.measurements[:, 0]
        self.time_values = self.measurements[:, 1]
        
        return self.measurements
    
    @staticmethod
    def _measure_time(func: Callable, data) -> float:
        """Measure execution time untuk single argument."""
        start = time.perf_counter()
        func(data)
        return time.perf_counter() - start
    
    @staticmethod
    def _measure_time_with_args(func: Callable, args: Tuple) -> float:
        """Measure execution time untuk multiple arguments."""
        start = time.perf_counter()
        func(*args)
        return time.perf_counter() - start
    
    def _fit_model(self, theoretical_values: np.ndarray) -> Dict:
        """Fit data empiris ke model linear: time = a*f(n) + b."""
        coeffs = np.polyfit(theoretical_values, self.time_values, 1)
        slope, intercept = coeffs[0], coeffs[1]
        
        predicted = slope * theoretical_values + intercept
        ss_res = np.sum((self.time_values - predicted) ** 2)
        ss_tot = np.sum((self.time_values - np.mean(self.time_values)) ** 2)
        r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        return {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_squared
        }
    
    def analyze_O1(self) -> Dict:
        """Analyze O(1) - Constant Time."""
        times = self.time_values
        variance = np.var(times)
        return {
            'class': 'O(1)',
            'r_squared': 1 - (variance / (np.var(times - np.mean(times)) + 1e-10))
        }
    
    def analyze_Ologn(self) -> Dict:
        """Analyze O(log n) - Logarithmic."""
        theoretical = np.log(self.n_values)
        result = self._fit_model(theoretical)
        result['class'] = 'O(log n)'
        return result
    
    def analyze_On(self) -> Dict:
        """Analyze O(n) - Linear."""
        theoretical = self.n_values
        result = self._fit_model(theoretical)
        result['class'] = 'O(n)'
        return result
    
    def analyze_Onlogn(self) -> Dict:
        """Analyze O(n log n) - Linearithmic."""
        theoretical = self.n_values * np.log(self.n_values)
        result = self._fit_model(theoretical)
        result['class'] = 'O(n log n)'
        return result
    
    def analyze_On2(self) -> Dict:
        """Analyze O(n^2) - Quadratic."""
        theoretical = self.n_values ** 2
        result = self._fit_model(theoretical)
        result['class'] = 'O(n^2)'
        return result
    
    def analyze_On3(self) -> Dict:
        """Analyze O(n^3) - Cubic."""
        theoretical = self.n_values ** 3
        result = self._fit_model(theoretical)
        result['class'] = 'O(n^3)'
        return result
    
    def analyze_all(self, func: Callable, data_gen: Callable, 
                    use_args: bool = False) -> Dict:
        """Analisis semua complexity classes dan return best fit."""
        self.collect_data(func, data_gen, use_args=use_args)
        
        results = [
            self.analyze_O1(),
            self.analyze_Ologn(),
            self.analyze_On(),
            self.analyze_Onlogn(),
            self.analyze_On2(),
            self.analyze_On3()
        ]
        
        results = sorted(results, key=lambda x: x['r_squared'], reverse=True)
        
        return {
            'best_fit': results[0]['class'],
            'confidence': results[0]['r_squared'],
            'all_results': results,
            'measurements': self.measurements
        }
    
    def print_results(self, analysis_result: Dict, title: str = "") -> None:
        """Print hasil analisis."""
        print("\n" + "="*70)
        if title:
            print("ANALYZING: " + title)
        print("="*70)
        
        print("\n[BEST FIT]: " + analysis_result['best_fit'])
        print("[CONFIDENCE (R^2)]: {:.6f}".format(analysis_result['confidence']))
        
        print("\n[RANKING]:")
        print("-" * 70)
        for rank, result in enumerate(analysis_result['all_results'], 1):
            r2 = result['r_squared']
            bar = "#" * int(r2 * 40) + "-" * (40 - int(r2 * 40))
            print("[{}] {} [{}] {:.4f}".format(rank, result['class'].ljust(12), bar, r2))
        
        print("\n[MEASUREMENTS]:")
        print("-" * 70)
        print("{:<10} {:<15}".format('n', 'Time (ms)'))
        for n, t in analysis_result['measurements'][:5]:  # Show first 5
            print("{:<10} {:<15.4f}".format(int(n), t * 1000))
        
        print("=" * 70 + "\n")
