"""
Historic Wealth Management Calculator
=====================================
Interactive script with hardcoded historic returns data (2000-2024)
No external Excel files required - all data embedded in the script

🎯 INTERACTIVE FEATURES:
- Enter your investment amount when prompted
- Set your desired asset allocation percentages
- Available asset classes: Global Equities, US Bonds, Cash
- Script calculates performance based on your inputs

Historic Data Period: 2000-2024 (25 years)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Tuple
import os
import warnings
warnings.filterwarnings('ignore')

class HistoricWealthCalculator:
    def __init__(self):
        """Initialize the historic calculator with hardcoded data"""
        
        # Currency setting
        self.currency = "USD"
        
        # Initialize variables (will be set by user input)
        self.investment_amount = None
        self.allocation = None
        
        # ======================================================================
        # 📊 HARDCODED HISTORIC DATA (2000-2024) - DO NOT MODIFY
        # ======================================================================
        
        # HARDCODED HISTORIC DATA (2000-2024)
        self.historic_data = {
            "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
            "Global Equities": ['−12.92%', '−16.52%', '−19.54%', 0.3376, 0.1525, 0.1002, 0.2065, 0.0957, '−40.33%', 0.3079, 0.1234, '−5.02%', 0.1654, 0.2737, 0.055, '−0.32%', 0.0815, 0.2307, '−8.20%', 0.284, 0.165, 0.2235, '−17.73%', 0.2442, 0.1919],
            "US Bonds": [0.1163, 0.0844, 0.1026, 0.041, 0.0434, 0.0243, 0.0433, 0.0697, 0.0524, 0.0593, 0.0654, 0.0784, 0.0421, '–2.02%', 0.0597, 0.0055, 0.0265, 0.0354, 0.0001, 0.0872, 0.0751, '–1.54%', '–13.01%', 0.0553, 0.0131],
            "Cash": [0.058198, 0.033994, 0.016053, 0.010084, 0.013746, 0.031492, 0.0473, 0.043620, 0.013713, 0.001505, 0.001384, 0.000528, 0.000876, 0.000571, 0.000327, 0.000520, 0.003161, 0.009341, 0.019363, 0.020625, 0.003547, 0.000450, 0.020248, 0.050704, 0.0497],
            "Inflation": [0.033868, 0.015517, 0.023769, 0.018795, 0.032556, 0.034157, 0.025407, 0.040813, 0.000914, 0.027213, 0.014957, 0.029624, 0.017410, 0.015017, 0.007565, 0.007295, 0.020746, 0.021091, 0.019102, 0.022851, 0.013620, 0.070364, 0.064544, 0.033521, 0.0275],
        }
        
        self.load_data()
    
    def get_user_investment_amount(self):
        """Get investment amount from user"""
        print(f"\n💰 INVESTMENT AMOUNT:")
        print("="*40)
        
        while True:
            try:
                amount_input = input(f"Enter your investment amount in {self.currency} (e.g., 100000): $")
                amount = float(amount_input.replace(',', '').replace('$', ''))
                
                if amount <= 0:
                    print("⚠️  Please enter a positive amount.")
                    continue
                    
                self.investment_amount = amount
                print(f"✅ Investment amount set: ${self.investment_amount:,.2f} {self.currency}")
                break
                
            except ValueError:
                print("⚠️  Please enter a valid number.")
    
    def get_user_allocation(self):
        """Get asset allocation from user"""
        print(f"\n🎯 ASSET ALLOCATION:")
        print("="*40)
        print("Available asset classes:")
        print("  1. Global Equities (stocks)")
        print("  2. US Bonds (bonds)")
        print("  3. Cash (cash equivalents)")
        print("\nAllocation percentages must sum to 100%")
        
        # Show example allocations
        print(f"\n💡 Example allocations:")
        print("  Conservative: 40% Equities, 50% Bonds, 10% Cash")
        print("  Moderate:     60% Equities, 35% Bonds,  5% Cash")
        print("  Aggressive:   80% Equities, 15% Bonds,  5% Cash")
        
        while True:
            try:
                print(f"\nEnter allocation percentages:")
                
                # Get Global Equities allocation
                equities_input = input("Global Equities %: ")
                equities_pct = float(equities_input.replace('%', ''))
                
                # Get US Bonds allocation
                bonds_input = input("US Bonds %: ")
                bonds_pct = float(bonds_input.replace('%', ''))
                
                # Get Cash allocation
                cash_input = input("Cash %: ")
                cash_pct = float(cash_input.replace('%', ''))
                
                # Validate total
                total_pct = equities_pct + bonds_pct + cash_pct
                
                if abs(total_pct - 100) > 0.1:
                    print(f"⚠️  Total allocation is {total_pct:.1f}% (must be 100%). Please try again.")
                    continue
                
                # Convert to decimals
                self.allocation = {
                    'Global Equities': equities_pct / 100,
                    'US Bonds': bonds_pct / 100,
                    'Cash': cash_pct / 100
                }
                
                print(f"\n✅ Allocation set:")
                for asset, weight in self.allocation.items():
                    if weight > 0:
                        print(f"   {asset}: {weight*100:.1f}%")
                print(f"   Total: {sum(self.allocation.values())*100:.1f}%")
                break
                
            except ValueError:
                print("⚠️  Please enter valid numbers.")
    
    def show_preset_allocations(self):
        """Show preset allocation options for quick selection"""
        print(f"\n🎯 QUICK ALLOCATION PRESETS:")
        print("="*40)
        
        presets = {
            '1': {'name': 'Conservative', 'Global Equities': 40, 'US Bonds': 50, 'Cash': 10},
            '2': {'name': 'Moderate', 'Global Equities': 60, 'US Bonds': 35, 'Cash': 5},
            '3': {'name': 'Aggressive', 'Global Equities': 80, 'US Bonds': 15, 'Cash': 5},
            '4': {'name': 'Growth', 'Global Equities': 90, 'US Bonds': 10, 'Cash': 0},
            '5': {'name': 'Bond-Heavy', 'Global Equities': 30, 'US Bonds': 65, 'Cash': 5},
            '6': {'name': 'Custom', 'Global Equities': 0, 'US Bonds': 0, 'Cash': 0}
        }
        
        for key, preset in presets.items():
            if key != '6':
                print(f"  {key}. {preset['name']}: {preset['Global Equities']}% Equities, {preset['US Bonds']}% Bonds, {preset['Cash']}% Cash")
            else:
                print(f"  {key}. {preset['name']}: Enter your own percentages")
        
        while True:
            choice = input(f"\nSelect allocation (1-6): ").strip()
            
            if choice in presets:
                if choice == '6':
                    # Custom allocation
                    self.get_user_allocation()
                else:
                    # Use preset
                    preset = presets[choice]
                    self.allocation = {
                        'Global Equities': preset['Global Equities'] / 100,
                        'US Bonds': preset['US Bonds'] / 100,
                        'Cash': preset['Cash'] / 100
                    }
                    print(f"\n✅ {preset['name']} allocation selected:")
                    for asset, weight in self.allocation.items():
                        if weight > 0:
                            print(f"   {asset}: {weight*100:.1f}%")
                break
            else:
                print("⚠️  Please enter a number between 1-6.")
        
    def validate_allocation(self):
        """Validate and display the user's asset allocation"""
        if not self.allocation or not self.investment_amount:
            return False
            
        total_allocation = sum(self.allocation.values())
        
        print(f"\n🔧 USER CONFIGURATION:")
        print(f"💰 Investment Amount: ${self.investment_amount:,} {self.currency}")
        print(f"📈 Analysis Type: HISTORIC (HARDCODED DATA)")
        print(f"🎯 Asset Allocation:")
        
        for asset, weight in self.allocation.items():
            if weight > 0:
                available = "✅" if asset in self.historic_df.columns else "❌"
                print(f"   {asset}: {weight*100:.1f}% {available}")
        
        print(f"   ───────────────────")
        print(f"   Total: {total_allocation*100:.1f}%")
        
        # Validation
        if abs(total_allocation - 1.0) > 0.01:
            print(f"⚠️  WARNING: Total allocation is {total_allocation*100:.1f}%")
            return False
        else:
            print(f"✅ Allocation validated: {total_allocation*100:.1f}%")
            return True
        
    def load_data(self):
        """Load and process hardcoded historic data"""
        try:
            print("Loading hardcoded historic data...")
            
            # Create DataFrame from hardcoded data
            self.historic_df = pd.DataFrame(self.historic_data)
            self.historic_df.set_index('Year', inplace=True)
            
            # Define asset columns
            self.asset_columns = ['Global Equities', 'US Bonds', 'Cash', 'Inflation']
            
            # Convert historic data to numeric, handling mixed formats
            for col in self.asset_columns:
                if col in self.historic_df.columns:
                    # Handle mixed format: some values are percentage strings, others are decimals
                    processed_values = []
                    for value in self.historic_df[col]:
                        if isinstance(value, str) and '%' in value:
                            # This is a percentage string - convert to decimal
                            clean_str = (str(value)
                                       .replace('%', '')
                                       .replace('−', '-')  # minus sign
                                       .replace('–', '-')  # en dash
                                       .replace('—', '-')  # em dash
                                       .replace(' ', '')   # remove spaces
                                       )
                            processed_values.append(pd.to_numeric(clean_str, errors='coerce') / 100)
                        else:
                            # This is already a decimal value (like 0.3376 = 33.76%)
                            processed_values.append(pd.to_numeric(value, errors='coerce'))
                    self.historic_df[col] = processed_values
            
            # Get available asset classes (exclude Inflation)
            self.available_assets = [col for col in self.asset_columns if col != 'Inflation']
            
            print("✅ Historic data loaded successfully!")
            print(f"📊 Available asset classes: {self.available_assets}")
            print(f"📅 Historic data period: {self.historic_df.index.min()} - {self.historic_df.index.max()}")
            
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            import traceback
            traceback.print_exc()
    
    def calculate_historic_returns(self, allocation: Dict[str, float], investment_amount: float) -> pd.DataFrame:
        """Calculate historic portfolio performance"""
        # Create a copy to avoid modifying original data
        df = self.historic_df.copy()
        
        # Calculate weighted portfolio return per year (only for assets that exist in data)
        df['Portfolio'] = sum(df[asset] * weight for asset, weight in allocation.items() if asset in df.columns)
        
        # Calculate real return (subtract inflation)
        df['Real_Portfolio'] = (1 + df['Portfolio']) / (1 + df['Inflation']) - 1
        
        # Cumulative returns
        df['Cumulative_Portfolio'] = (1 + df['Portfolio']).cumprod() * investment_amount
        df['Cumulative_Inflation'] = (1 + df['Inflation']).cumprod() * investment_amount
        
        return df
    
    def create_historic_visualizations(self, df: pd.DataFrame, investment_amount: float):
        """Create visualizations for historic returns"""
        # Set style
        plt.style.use('default')
        
        # Line chart: Portfolio vs Inflation
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['Cumulative_Portfolio'], label='Portfolio Value', linewidth=2, color='blue')
        plt.plot(df.index, df['Cumulative_Inflation'], label='Inflation-Adjusted Value', linewidth=2, color='red')
        plt.title("Portfolio Performance vs Inflation (Cumulative Return)", fontsize=16, fontweight='bold')
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Value (USD)", fontsize=12)
        plt.legend(fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        # Bar chart: Annual real returns
        plt.figure(figsize=(14, 6))
        colors = ['green' if x > 0 else 'red' for x in df['Real_Portfolio']]
        plt.bar(df.index, df['Real_Portfolio'] * 100, color=colors, alpha=0.7)
        plt.title("Annual Real Portfolio Returns", fontsize=16, fontweight='bold')
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Real Return (%)", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        # Drawdown Analysis
        self.create_drawdown_chart(df, investment_amount)
        
        # Rolling Returns Analysis
        self.create_rolling_returns_chart(df)
    
    def create_drawdown_chart(self, df: pd.DataFrame, investment_amount: float):
        """Create drawdown analysis chart"""
        # Calculate drawdown
        cumulative_returns = df['Cumulative_Portfolio']
        peak = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - peak) / peak * 100
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Portfolio value with peaks
        ax1.plot(df.index, cumulative_returns, label='Portfolio Value', linewidth=2, color='blue')
        ax1.plot(df.index, peak, label='Previous Peak', linewidth=1, color='green', alpha=0.7)
        ax1.set_title("Portfolio Value vs Peak Values", fontsize=14, fontweight='bold')
        ax1.set_ylabel("Value (USD)", fontsize=12)
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Drawdown chart
        ax2.fill_between(df.index, drawdown, 0, color='red', alpha=0.3, label='Drawdown')
        ax2.plot(df.index, drawdown, color='red', linewidth=1)
        ax2.set_title("Drawdown Analysis", fontsize=14, fontweight='bold')
        ax2.set_xlabel("Year", fontsize=12)
        ax2.set_ylabel("Drawdown (%)", fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        # Add max drawdown annotation
        max_drawdown = drawdown.min()
        max_dd_date = drawdown.idxmin()
        ax2.annotate(f'Max Drawdown: {max_drawdown:.1f}%', 
                    xy=(max_dd_date, max_drawdown), 
                    xytext=(max_dd_date + 2, max_drawdown + 5),
                    arrowprops=dict(arrowstyle='->', color='black'),
                    fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        # Print drawdown statistics
        print(f"\nDrawdown Analysis:")
        print(f"  Maximum Drawdown: {max_drawdown:.2f}%")
        print(f"  Occurred in: {max_dd_date}")
        
        # Calculate recovery times
        drawdowns_below_5 = drawdown[drawdown < -5]
        if len(drawdowns_below_5) > 0:
            print(f"  Periods with >5% drawdown: {len(drawdowns_below_5)} years")
    
    def create_rolling_returns_chart(self, df: pd.DataFrame):
        """Create rolling returns analysis"""
        # Calculate rolling returns
        returns = df['Real_Portfolio']
        rolling_3yr = returns.rolling(window=3).mean() * 100
        rolling_5yr = returns.rolling(window=5).mean() * 100
        rolling_10yr = returns.rolling(window=10).mean() * 100
        
        plt.figure(figsize=(14, 8))
        
        plt.plot(df.index, rolling_3yr, label='3-Year Rolling Average', linewidth=2, alpha=0.8)
        plt.plot(df.index, rolling_5yr, label='5-Year Rolling Average', linewidth=2, alpha=0.8)
        plt.plot(df.index, rolling_10yr, label='10-Year Rolling Average', linewidth=2, alpha=0.8)
        
        plt.title("Rolling Average Returns", fontsize=16, fontweight='bold')
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Annualized Return (%)", fontsize=12)
        plt.legend(fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        
        # Add some statistics
        mean_3yr = rolling_3yr.mean()
        mean_5yr = rolling_5yr.mean()
        mean_10yr = rolling_10yr.mean()
        
        plt.axhline(y=mean_3yr, color='blue', linestyle='--', alpha=0.5)
        plt.axhline(y=mean_5yr, color='orange', linestyle='--', alpha=0.5)
        plt.axhline(y=mean_10yr, color='green', linestyle='--', alpha=0.5)
        
        plt.tight_layout()
        plt.show()
        
        print(f"\nRolling Returns Analysis:")
        print(f"  Average 3-Year Return: {mean_3yr:.2f}%")
        print(f"  Average 5-Year Return: {mean_5yr:.2f}%")
        print(f"  Average 10-Year Return: {mean_10yr:.2f}%")
    
    def calculate_historic_summary(self, df: pd.DataFrame, investment_amount: float) -> pd.DataFrame:
        """Calculate summary statistics for historic returns"""
        final_value = df['Cumulative_Portfolio'].iloc[-1]
        years = len(df)
        
        # Calculate total return over the period
        total_return = (final_value / investment_amount) - 1
        
        # Calculate CAGR (Compound Annual Growth Rate)
        cagr = (final_value / investment_amount) ** (1 / years) - 1
        
        summary = {
            "Initial Investment (USD)": investment_amount,
            "Final Value (USD)": final_value,
            "Total Return (%)": total_return * 100,
            "CAGR (%)": cagr * 100,
            "Arithmetic Mean (%)": df['Real_Portfolio'].mean() * 100,
            "Standard Deviation (%)": df['Real_Portfolio'].std() * 100,
            "Best Year (%)": df['Real_Portfolio'].max() * 100,
            "Worst Year (%)": df['Real_Portfolio'].min() * 100,
            "Years Analyzed": years,
            "Positive Years": len(df[df['Real_Portfolio'] > 0]),
            "Negative Years": len(df[df['Real_Portfolio'] < 0])
        }
        
        return pd.DataFrame(summary, index=["Value"]).T
    
    def show_individual_asset_performance(self) -> pd.DataFrame:
        """Show performance statistics for each individual asset class"""
        print(f"\n📊 INDIVIDUAL ASSET CLASS PERFORMANCE (2000-2024):")
        print("="*60)
        
        asset_stats = {}
        
        for asset in self.available_assets:
            if asset in self.historic_df.columns:
                returns = self.historic_df[asset]
                
                # Calculate statistics
                total_return = (1 + returns).prod() - 1
                cagr = (1 + returns).prod() ** (1/len(returns)) - 1
                mean_return = returns.mean()
                volatility = returns.std()
                best_year = returns.max()
                worst_year = returns.min()
                positive_years = len(returns[returns > 0])
                negative_years = len(returns[returns < 0])
                
                asset_stats[asset] = {
                    'Total Return (%)': total_return * 100,
                    'CAGR (%)': cagr * 100,
                    'Average Return (%)': mean_return * 100,
                    'Volatility (%)': volatility * 100,
                    'Best Year (%)': best_year * 100,
                    'Worst Year (%)': worst_year * 100,
                    'Positive Years': positive_years,
                    'Negative Years': negative_years
                }
        
        asset_df = pd.DataFrame(asset_stats).T
        print(asset_df.round(2))
        
        return asset_df
    
    def create_performance_attribution(self, df: pd.DataFrame, allocation: Dict[str, float]):
        """Create performance attribution analysis"""
        # Calculate contribution of each asset to total return
        contributions = {}
        total_portfolio_return = 0
        
        for asset, weight in allocation.items():
            if asset in df.columns:
                asset_contribution = (df[asset] * weight).sum()
                contributions[asset] = asset_contribution
                total_portfolio_return += asset_contribution
        
        # Convert to percentages of total return
        contribution_pcts = {asset: (contrib/total_portfolio_return)*100 if total_portfolio_return != 0 else 0 
                           for asset, contrib in contributions.items()}
        
        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Bar chart of absolute contributions
        assets = list(contributions.keys())
        values = list(contributions.values())
        colors = plt.cm.Set3(np.linspace(0, 1, len(assets)))
        
        bars1 = ax1.bar(assets, values, color=colors, alpha=0.8)
        ax1.set_title("Total Return Contribution by Asset", fontsize=14, fontweight='bold')
        ax1.set_ylabel("Cumulative Return Contribution", fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar, value in zip(bars1, values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{value:.3f}', ha='center', va='bottom', fontsize=10)
        
        # Pie chart of percentage contributions
        positive_contributions = {k: v for k, v in contribution_pcts.items() if v > 0}
        if positive_contributions:
            wedges, texts, autotexts = ax2.pie(positive_contributions.values(), 
                                             labels=positive_contributions.keys(),
                                             colors=colors[:len(positive_contributions)],
                                             autopct='%1.1f%%', 
                                             startangle=90)
            ax2.set_title("Percentage Contribution to Total Return", fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
        # Print attribution analysis
        print(f"\n📊 Performance Attribution Analysis:")
        print(f"  Total Portfolio Return: {total_portfolio_return:.4f}")
        for asset, contrib in contributions.items():
            weight = allocation.get(asset, 0)
            pct_contrib = contribution_pcts.get(asset, 0)
            print(f"  {asset}: {contrib:.4f} ({pct_contrib:.1f}% of total, {weight*100:.1f}% allocation)")
        
        # Calculate asset efficiency (return per unit of allocation)
        print(f"\n  💡 Asset Efficiency (Return/Allocation):")
        for asset, contrib in contributions.items():
            weight = allocation.get(asset, 0)
            if weight > 0:
                efficiency = contrib / weight
                print(f"  {asset}: {efficiency:.4f}")
    
    def run_interactive_calculator(self):
        """Interactive method to get user inputs and run analysis"""
        print(f"\n" + "="*60)
        print("🚀 INTERACTIVE HISTORIC WEALTH CALCULATOR")
        print("="*60)
        print("Welcome! Let's analyze your portfolio's historic performance.")
        print(f"Historic data period: 2000-2024 (25 years)")
        
        # Get user inputs
        self.get_user_investment_amount()
        self.show_preset_allocations()
        
        # Validate configuration
        if not self.validate_allocation():
            print("❌ Configuration error. Please restart the calculator.")
            return
        
        # Ask if user wants to proceed
        print(f"\n🚀 Ready to analyze your portfolio performance!")
        proceed = input("Continue with analysis? (y/n): ").lower().strip()
        
        if proceed not in ['y', 'yes']:
            print("Analysis cancelled.")
            return
        
        # Run the analysis
        self.run_calculator()
    
    def run_calculator(self):
        """Main function to run the historic calculator"""
        try:
            print(f"\n" + "="*60)
            print("📊 HISTORIC WEALTH CALCULATOR - ANALYSIS RESULTS")
            print("="*60)
            print(f"💰 Investment Amount: ${self.investment_amount:,.2f} {self.currency}")
            print(f"📈 Analysis Type: HISTORIC PERFORMANCE (2000-2024)")
            print("🎯 Your Asset Allocation:")
            for asset, weight in self.allocation.items():
                if weight > 0:
                    print(f"   {asset}: {weight*100:.1f}%")
            
            # Show individual asset performance first
            print("\n� Individual Asset Class Performance...")
            self.show_individual_asset_performance()
            
            print("\n�📊 Running Portfolio Analysis...")
            
            # Historic analysis
            df = self.calculate_historic_returns(self.allocation, self.investment_amount)
            self.create_historic_visualizations(df, self.investment_amount)
            
            # Performance Attribution
            print("\n🔍 Generating Performance Attribution Analysis...")
            self.create_performance_attribution(df, self.allocation)
            
            # Summary
            summary = self.calculate_historic_summary(df, self.investment_amount)
            print(f"\n📋 YOUR PORTFOLIO PERFORMANCE SUMMARY:")
            print("="*50)
            print(summary.round(2))
            
            print(f"\n✅ Historic analysis complete!")
            print(f"\n💡 This analysis shows how your portfolio would have performed from 2000-2024")
                
        except Exception as e:
            print(f"❌ Error in calculation: {e}")
            import traceback
            traceback.print_exc()

# Initialize and run the interactive calculator
if __name__ == "__main__":
    calculator = HistoricWealthCalculator()
    calculator.run_interactive_calculator()
