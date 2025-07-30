#!/usr/bin/env python3

"""
Capital Markets Calculator - Interactive Future Projections
A comprehensive wealth management tool for forward-looking portfolio analysis.
This calculator provides Monte Carlo simulations and risk analysis for various asset classes.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class CapitalMarketsCalculator:
    """Interactive Capital Markets Calculator for future portfolio projections"""
    
    def __init__(self):
        self.investment_amount = 0
        self.allocation = {}
        self.currency = "USD"
        self.time_horizon = 10  # years
        self.num_simulations = 10000
        self.return_type = "real"  # "real" or "nominal"
        self.inflation_rate = 0.030  # 3.0% annual inflation assumption
        
        # Initialize asset data dictionaries
        self.asset_data_nominal = {
            'Global Equity': {'Expected Return': 0.0800, 'Volatility': 0.1650},
            'Global Bonds': {'Expected Return': 0.0400, 'Volatility': 0.0600},
            'Global Private Real Estate': {'Expected Return': 0.1200, 'Volatility': 0.1400},
            'Global Private Debt': {'Expected Return': 0.0800, 'Volatility': 0.1000},
            'Global Diversified Alternatives': {'Expected Return': 0.1100, 'Volatility': 0.1200},
            'Global VC': {'Expected Return': 0.1300, 'Volatility': 0.3000},
            'Guaranteed Return USD': {'Expected Return': 0.0625, 'Volatility': 0.0200},
            'Guaranteed Investment USD': {'Expected Return': 0.0700, 'Volatility': 0.0200},
            'Autocall Capital Protected USD': {'Expected Return': 0.0800, 'Volatility': 0.0250},
            'USD Cash': {'Expected Return': 0.0450, 'Volatility': 0.0200}
        }
        
        # Set available assets
        self.available_assets = list(self.asset_data_nominal.keys())
    
    def load_capital_markets_data(self):
        """Load capital markets data"""
        try:
            # Calculate real returns by subtracting inflation rate
            self.asset_data_real = {
                'Global Equity': {'Expected Return': 0.0500, 'Volatility': 0.1650},
                'Global Bonds': {'Expected Return': 0.0100, 'Volatility': 0.0600},
                'Global Private Real Estate': {'Expected Return': 0.0900, 'Volatility': 0.1400},
                'Global Private Debt': {'Expected Return': 0.0500, 'Volatility': 0.1000},
                'Global Diversified Alternatives': {'Expected Return': 0.0800, 'Volatility': 0.1200},
                'Global VC': {'Expected Return': 0.1000, 'Volatility': 0.3000},
                'Guaranteed Return USD': {'Expected Return': 0.0325, 'Volatility': 0.0200},
                'Guaranteed Investment USD': {'Expected Return': 0.0400, 'Volatility': 0.0200},
                'Autocall Capital Protected USD': {'Expected Return': 0.0500, 'Volatility': 0.0250},
                'USD Cash': {'Expected Return': 0.0150, 'Volatility': 0.0200}
            }

            # Set available assets
            self.available_assets = list(self.asset_data_nominal.keys())
            
            print("✅ Capital markets data loaded successfully!")
            
        except Exception as e:
            print(f"❌ Error loading capital markets data: {e}")
            raise
    
    def setup_calculator(self):
        """Interactive setup for the calculator"""
        print("="*60)
        print("📊 CAPITAL MARKETS CALCULATOR - FUTURE PROJECTIONS")
        print("="*60)
        print("Welcome to the interactive Capital Markets Calculator!")
        print("This tool provides forward-looking projections using capital markets expectations.")
        print("\n🔮 Based on SWAN Capital Markets Data (from Excel)")
        print(f"📅 Analysis Period: {self.time_horizon} years")
        print(f"🎲 Monte Carlo Simulations: {self.num_simulations:,}")
        print(f"📊 Return Types: Nominal vs Real (from Excel columns)")
        print(f"💹 Inflation Rate: 3.0% (from Excel data)")
        
        # Get investment amount
        self.get_investment_amount()
        # Get return type preference
        self.get_return_type()
        # Get allocation
        self.show_preset_allocations()
        # Validate and proceed
        if self.validate_allocation():
            self.run_calculator()
        else:
            print("❌ Setup incomplete. Please restart the calculator.")
    
    def get_investment_amount(self):
        """Get investment amount from user"""
        print(f"\n💰 INVESTMENT AMOUNT:")
        print("="*40)
        while True:
            try:
                amount_input = input("Enter your investment amount (USD): $")
                # Remove any formatting characters
                amount_str = amount_input.replace(',', '').replace('$', '').strip()
                amount = float(amount_str)
                
                if amount <= 0:
                    print("⚠️  Please enter a positive amount.")
                    continue
                self.investment_amount = amount
                print(f"✅ Investment amount set: ${self.investment_amount:,.2f} USD")
                break
            except ValueError:
                print("⚠️  Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n❌ Setup cancelled.")
                exit()
    
    def get_return_type(self):
        """Get return type preference from user"""
        print(f"\n📊 RETURN TYPE SELECTION:")
        print("="*40)
        print("Choose the type of returns for your analysis:")
        print("  1. Real Returns (from Excel 'Real Return' column)")
        print("  2. Nominal Returns (from Excel 'Nominal Return' column)")
        print(f"\n💡 Inflation rate from Excel: {self.inflation_rate*100:.1f}% annually")
        
        while True:
            choice = input(f"\nSelect return type (1-2): ").strip()
            
            if choice == "1":    
                self.return_type = "real"
                print("✅ Real returns selected (from Excel 'Real Return' column)")
                break
            elif choice == "2":
                self.return_type = "nominal"
                print("✅ Nominal returns selected (from Excel 'Nominal Return' column)")
                break
            else:
                print("⚠️  Please enter 1 or 2.")
    
    @property
    def asset_data(self):
        """Return the appropriate asset data based on return type"""
        return self.asset_data_real if self.return_type == "real" else self.asset_data_nominal
    
    def show_asset_classes(self):
        """Display available asset classes with their expected returns and volatilities"""
        print(f"\n📋 AVAILABLE ASSET CLASSES:")
        print("="*70)
        print(f"{'#':<3} {'Asset Class':<35} {'Exp. Return':<12} {'Volatility':<10}")
        print("-" * 70)
        for i, asset in enumerate(self.available_assets):
            ret = self.asset_data[asset]['Expected Return'] * 100
            vol = self.asset_data[asset]['Volatility'] * 100
            print(f"{i+1:<3} {asset:<35} {ret:>6.1f}%{'':<8} {vol:>5.1f}%")
    
    def get_user_allocation(self):
        """Get asset allocation from user with support for multiple assets"""
        print(f"\n🎯 ASSET ALLOCATION:")
        print("="*40)
        print("Enter the asset numbers and allocation percentages for your portfolio.")
        print("Allocation percentages must sum to 100%")
        print("Enter 0 when finished adding assets.")
        
        self.allocation = {}
        total_allocated = 0
        
        while True:
            try:
                # Show current allocation
                if self.allocation:
                    print(f"\nCurrent allocation:")
                    for asset, weight in self.allocation.items():
                        print(f"  {asset}: {weight*100:.1f}%")
                    print(f"  Total allocated: {total_allocated:.1f}%")
                    print(f"  Remaining: {100-total_allocated:.1f}%")
                
                # Get asset selection
                asset_input = input(f"\nEnter asset number (1-{len(self.available_assets)}, or 0 to finish): ")
                asset_num = int(asset_input)
                if asset_num == 0:
                    break
                if asset_num < 1 or asset_num > len(self.available_assets):
                    print(f"⚠️  Please enter a number between 1-{len(self.available_assets)}")
                    continue
                asset_name = self.available_assets[asset_num - 1]
                
                if asset_name in self.allocation:
                    print(f"⚠️  {asset_name} already allocated. Skipping...")
                    continue
                
                # Get allocation percentage
                remaining = 100 - total_allocated
                pct_input = input(f"Enter allocation % for {asset_name} (remaining: {remaining:.1f}%): ")
                pct = float(pct_input.replace('%', ''))
                
                if pct <= 0:
                    print("⚠️  Please enter a positive percentage.")
                    continue
                if total_allocated + pct > 100.1:
                    print(f"⚠️  This would exceed 100% allocation. Maximum remaining: {remaining:.1f}%")
                    continue
                # Add to allocation
                self.allocation[asset_name] = pct / 100
                total_allocated += pct
                
                print(f"✅ Added {asset_name}: {pct:.1f}%")
                
                # Check if we've reached 100%
                if abs(total_allocated - 100) < 0.1:
                    print("✅ Allocation complete (100%)")
                    break
            except ValueError:
                print("⚠️  Please enter valid numbers.")
            except KeyboardInterrupt:
                print("\n❌ Input cancelled.")
                break
    
    def show_preset_allocations(self):
        """Show preset allocation options for quick selection"""
        print(f"\n🎯 QUICK ALLOCATION PRESETS:")
        print("="*40)
        
        presets = {
            '1': {'name': 'Conservative Growth', 'Global Equity': 30, 'Global Bonds': 60, 'USD Cash': 10},
            '2': {'name': 'Moderate Growth', 'Global Equity': 50, 'Global Bonds': 40, 'USD Cash': 10},
            '3': {'name': 'Aggressive Growth', 'Global Equity': 70, 'Global Bonds': 25, 'USD Cash': 5},
            '4': {'name': 'Diversified Alternative', 'Global Equity': 40, 'Global Bonds': 30, 'Global Diversified Alternatives': 20, 'USD Cash': 10},
            '5': {'name': 'Private Markets', 'Global Equity': 30, 'Global Private Real Estate': 25, 'Global Private Debt': 25, 'Global Bonds': 15, 'USD Cash': 5},
            '6': {'name': 'Custom', 'description': 'Build your own allocation'}
        }
        
        for key, preset in presets.items():
            if key != '6':
                assets_str = ', '.join([f"{pct}% {asset}" for asset, pct in preset.items() if asset != 'name'])
                print(f"  {key}. {preset['name']}: {assets_str}")
            else:
                print(f"  {key}. {preset['name']}: {preset['description']}")
        
        while True:
            choice = input(f"\nSelect allocation (1-6): ").strip()
            
            if choice in presets:
                if choice == '6':
                    # Custom allocation
                    self.show_asset_classes()
                    success = self.get_user_allocation()
                    if success:
                        break
                else:
                    # Use preset
                    preset = presets[choice]
                    self.allocation = {}
                    for asset, pct in preset.items():
                        if asset != 'name':
                            self.allocation[asset] = pct / 100
                    print(f"\n✅ {preset['name']} allocation selected:")
                    for asset, weight in self.allocation.items():
                        print(f"   {asset}: {weight*100:.1f}%")
                    break
            else:
                print("⚠️  Please enter a number between 1-6.")
    
    def validate_allocation(self):
        """Validate the user allocation"""
        total_allocation = sum(self.allocation.values())
        
        if abs(total_allocation - 1.0) > 0.001:
            print("❌ Error: Total allocation must equal 100%")
            return False
        
        return True
    
    def run_calculator(self):
        """Main function to run the capital markets calculator"""
        try:
            print(f"\n" + "="*60)
            print("📊 CAPITAL MARKETS CALCULATOR - FUTURE PROJECTIONS")
            print("="*60)
            print(f"💰 Investment Amount: ${self.investment_amount:,.2f} {self.currency}")
            print(f"📈 Analysis Type: FORWARD-LOOKING PROJECTIONS")
            print(f"📊 Return Type: {'Real (Inflation-Adjusted)' if self.return_type == 'real' else 'Nominal (Including Inflation)'}")
            if self.return_type == "nominal":
                print(f"💹 Inflation Assumption: {self.inflation_rate*100:.1f}% annually")
            print("🎯 Your Asset Allocation:")
            for asset, weight in self.allocation.items():
                if weight > 0:
                    print(f"   {asset}: {weight*100:.1f}%")
            
            # Portfolio statistics
            print(f"\n📊 PORTFOLIO STATISTICS:")
            expected_return = 0
            portfolio_variance = 0
            for asset, weight in self.allocation.items():
                exp_ret = self.asset_data[asset]['Expected Return'] * 100
                vol = self.asset_data[asset]['Volatility'] * 100
                print(f"  {asset}: {weight*100:.1f}% (Exp: {exp_ret:.1f}%, Vol: {vol:.1f}%)")
                expected_return += weight * self.asset_data[asset]['Expected Return']
                portfolio_variance += (weight ** 2) * (self.asset_data[asset]['Volatility'] ** 2)
            
            portfolio_volatility = np.sqrt(portfolio_variance)
            
            print(f"   📈 Expected Annual Return: {expected_return*100:.2f}% ({'Real' if self.return_type == 'real' else 'Nominal'})")
            print(f"   📉 Portfolio Volatility: {portfolio_volatility*100:.2f}%")
            risk_free_rate = self.asset_data['USD Cash']['Expected Return']  # Using cash rate as risk-free
            sharpe_ratio = (expected_return - risk_free_rate) / portfolio_volatility
            print(f"   📊 Sharpe Ratio: {sharpe_ratio:.2f}")
            
            # Run Monte Carlo Simulation
            print(f"\n🎲 MONTE CARLO SIMULATION ({self.num_simulations:,} simulations):")
            
            final_values = []
            yearly_values = []  # Store year-by-year progression for additional charts
            for simulation in range(self.num_simulations):
                value = self.investment_amount
                year_path = [value]
                for year in range(self.time_horizon):
                    annual_return = np.random.normal(expected_return, portfolio_volatility)
                    value *= (1 + annual_return)
                    year_path.append(value)
                
                final_values.append(value)
                yearly_values.append(year_path)
            final_values = np.array(final_values)
            
            # Calculate statistics
            mean_value = np.mean(final_values)
            median_value = np.median(final_values)
            p10_value = np.percentile(final_values, 10)
            p90_value = np.percentile(final_values, 90)
            
            print(f"   💰 Expected Value (Mean): ${mean_value:,.2f} {self.currency}")
            print(f"   📊 Median Value: ${median_value:,.2f} {self.currency}")
            print(f"   📉 10th Percentile: ${p10_value:,.2f} {self.currency}")
            print(f"   📈 90th Percentile: ${p90_value:,.2f} {self.currency}")
            
            # Calculate returns
            mean_return = ((mean_value / self.investment_amount) ** (1/self.time_horizon) - 1) * 100
            total_return = ((mean_value / self.investment_amount) - 1) * 100
            
            print(f"\n📈 PROJECTED RETURNS ({'Real' if self.return_type == 'real' else 'Nominal'}):")
            print(f"   💹 Annualized Return: {mean_return:.2f}% per year")
            print(f"   💰 Total Return: {total_return:.2f}% over {self.time_horizon} years")
            print(f"   💵 Total Gain: ${mean_value - self.investment_amount:,.2f} {self.currency}")
            
            # Calculate real purchasing power if using nominal returns
            if self.return_type == "nominal":
                real_final_values = final_values / ((1 + self.inflation_rate) ** self.time_horizon)
                real_mean_value = np.mean(real_final_values)
                real_mean_return = ((real_mean_value / self.investment_amount) ** (1/self.time_horizon) - 1) * 100
                
                print(f"\n💰 REAL PURCHASING POWER (Inflation-Adjusted):")
                print(f"   💰 Real Value (Mean): ${real_mean_value:,.2f} {self.currency}")
                print(f"   💹 Real Annualized Return: {real_mean_return:.2f}% per year")
            
            # Create comprehensive visualizations
            self.create_comprehensive_charts(final_values, yearly_values, mean_value, median_value, p10_value, p90_value)
            
            print(f"\n✅ Capital markets projections analysis complete!")
        except Exception as e:
            print(f"❌ Error in calculation: {e}")
            import traceback
            traceback.print_exc()
    
    def create_comprehensive_charts(self, final_values, yearly_values, mean_value, median_value, p10_value, p90_value):
        """Create comprehensive visualization suite for projections"""
        try:
            import matplotlib.pyplot as plt
            # Create a figure with multiple subplots
            fig = plt.figure(figsize=(20, 15))
            

            # 1. Distribution histogram (top left)
            ax1 = plt.subplot(3, 3, 1)
            ax1.hist(final_values, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
            ax1.axvline(mean_value, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_value:,.0f}')
            ax1.axvline(median_value, color='orange', linestyle='--', linewidth=2, label=f'Median: ${median_value:,.0f}')
            ax1.axvline(p10_value, color='purple', linestyle='--', linewidth=1, label=f'10th %: ${p10_value:,.0f}')
            ax1.axvline(p90_value, color='green', linestyle='--', linewidth=1, label=f'90th %: ${p90_value:,.0f}')
            ax1.set_xlabel(f'Portfolio Value after {self.time_horizon} years')
            ax1.set_ylabel('Frequency')
            ax1.set_title(f'Distribution of Final Values\n({self.num_simulations:,} Simulations)')
            ax1.legend(fontsize=8)
            ax1.grid(True, alpha=0.3)
            # 2. Box plot (top center)    
            ax2 = plt.subplot(3, 3, 2)
            ax2.boxplot(final_values, vert=True)
            ax2.set_ylabel(f'Portfolio Value after {self.time_horizon} years')
            ax2.set_title('Value Distribution Summary')
            ax2.grid(True, alpha=0.3)
            # 3. Percentile progression over time (top right)
            ax3 = plt.subplot(3, 3, 3)
            yearly_array = np.array(yearly_values)
            years = list(range(self.time_horizon + 1))
            
            # Calculate percentiles for each year
            p10_progression = [np.percentile(yearly_array[:, year], 10) for year in range(self.time_horizon + 1)]
            p25_progression = [np.percentile(yearly_array[:, year], 25) for year in range(self.time_horizon + 1)]
            p50_progression = [np.percentile(yearly_array[:, year], 50) for year in range(self.time_horizon + 1)]
            p75_progression = [np.percentile(yearly_array[:, year], 75) for year in range(self.time_horizon + 1)]
            p90_progression = [np.percentile(yearly_array[:, year], 90) for year in range(self.time_horizon + 1)]
            ax3.fill_between(years, p10_progression, p90_progression, alpha=0.2, color='blue', label='10th-90th %')
            ax3.fill_between(years, p25_progression, p75_progression, alpha=0.4, color='green', label='25th-75th %')
            ax3.plot(years, p50_progression, color='red', linewidth=2, label='Median')
            ax3.set_xlabel('Years')
            ax3.set_ylabel('Portfolio Value')
            ax3.set_title('Value Progression Over Time\n(Confidence Bands)')
            ax3.legend(fontsize=8)
            ax3.grid(True, alpha=0.3)
            # 4. Sample paths (middle left)
            ax4 = plt.subplot(3, 3, 4)
            sample_paths = yearly_values[:100]  # Show first 100 simulations
            for path in sample_paths:
                ax4.plot(years, path, alpha=0.1, color='blue')
            ax4.plot(years, p50_progression, color='red', linewidth=3, label='Median Path')
            ax4.set_xlabel('Years')
            ax4.set_ylabel('Portfolio Value')
            ax4.set_title('Sample Simulation Paths\n(100 Random Simulations)')
            ax4.legend(fontsize=8)
            ax4.grid(True, alpha=0.3)
            # 5. Return distribution (middle center)
            ax5 = plt.subplot(3, 3, 5)
            annual_returns = [(val/self.investment_amount)**(1/self.time_horizon) - 1 for val in final_values]
            ax5.hist(annual_returns, bins=50, alpha=0.7, color='lightcoral', edgecolor='black')
            mean_annual_return = np.mean(annual_returns)
            ax5.axvline(mean_annual_return, color='red', linestyle='--', linewidth=2, 
                       label=f'Mean: {mean_annual_return*100:.2f}%')
            ax5.set_xlabel('Annualized Return')
            ax5.set_ylabel('Frequency')
            ax5.set_title(f'Distribution of Annualized Returns\n({self.return_type.title()} Returns)')
            ax5.legend(fontsize=8)
            ax5.grid(True, alpha=0.3)
            ax5.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x*100:.1f}%'))
            
            # 6. Probability of positive returns (middle right)
            ax6 = plt.subplot(3, 3, 6)
            positive_returns = [ret > 0 for ret in annual_returns]
            prob_positive = np.mean(positive_returns) * 100
            
            negative_returns = [ret < 0 for ret in annual_returns]
            prob_negative = np.mean(negative_returns) * 100
            
            categories = ['Positive Returns', 'Negative Returns']
            probabilities = [prob_positive, prob_negative]
            colors = ['green', 'red']
            
            bars = ax6.bar(categories, probabilities, color=colors, alpha=0.7)
            ax6.set_ylabel('Probability (%)')
            ax6.set_title(f'Probability of Return Outcomes\n(Over {self.time_horizon} Years)')
            ax6.grid(True, alpha=0.3)
            # Add percentage labels on bars
            for bar, prob in zip(bars, probabilities):
                height = bar.get_height()
                ax6.text(bar.get_x() + bar.get_width()/2., height + 1,
                        f'{prob:.1f}%', ha='center', va='bottom', fontweight='bold')
            # 7. Value at Risk analysis (bottom left)
            ax7 = plt.subplot(3, 3, 7)
            var_levels = [1, 5, 10, 25, 50, 75, 90, 95, 99]
            var_values = [np.percentile(final_values, level) for level in var_levels]
            
            ax7.plot(var_levels, var_values, 'o-', color='purple', linewidth=2, markersize=6)
            ax7.axhline(self.investment_amount, color='red', linestyle='--', alpha=0.7, label='Initial Investment')
            ax7.set_xlabel('Percentile')
            ax7.set_ylabel('Portfolio Value')
            ax7.set_title('Value at Risk (VaR) Analysis')
            ax7.legend(fontsize=8)
            ax7.grid(True, alpha=0.3)
            # 8. Growth multiple distribution (bottom center)
            ax8 = plt.subplot(3, 3, 8)
            growth_multiples = [val/self.investment_amount for val in final_values]
            ax8.hist(growth_multiples, bins=50, alpha=0.7, color='gold', edgecolor='black')
            mean_multiple = np.mean(growth_multiples)
            ax8.axvline(mean_multiple, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_multiple:.2f}x')
            ax8.axvline(1.0, color='black', linestyle='-', alpha=0.5, label='Break-even')
            ax8.set_xlabel('Growth Multiple')
            ax8.set_ylabel('Frequency')
            ax8.set_title(f'Portfolio Growth Multiple\n(Final Value / Initial Investment)')
            ax8.legend(fontsize=8)
            ax8.grid(True, alpha=0.3)
            # 9. Asset allocation pie chart (bottom right)
            ax9 = plt.subplot(3, 3, 9)
            allocation_labels = []
            allocation_sizes = []
            colors_pie = plt.cm.Set3(np.linspace(0, 1, len(self.allocation)))
            for asset, weight in self.allocation.items():
                if weight > 0:
                    allocation_labels.append(f'{asset}\n{weight*100:.1f}%')
                    allocation_sizes.append(weight)
            
            ax9.pie(allocation_sizes, labels=allocation_labels, colors=colors_pie,
                   autopct='', startangle=90, textprops={'fontsize': 8})
            ax9.set_title(f'Portfolio Allocation\n({self.return_type.title()} Returns)')
            
            # Format y-axes for financial values
            for ax in [ax1, ax2, ax3, ax4, ax7]:
                ax.yaxis.set_major_formatter(plt.FuncFormatter(
                    lambda x, p: f'${x/1e6:.1f}M' if x >= 1e6 else f'${x/1e3:.0f}K'))
            
            plt.suptitle(f'Capital Markets Calculator - Comprehensive Analysis\n'
                        f'${self.investment_amount:,.0f} Investment | {self.time_horizon} Years | '
                        f'{self.return_type.title()} Returns', fontsize=16, fontweight='bold')
            
            plt.tight_layout()
            plt.subplots_adjust(top=0.93)
            plt.show()
        except ImportError:
            print("📊 Matplotlib not available for comprehensive visualization")
            # Fallback to simple text-based analysis
            self.create_text_analysis(final_values, mean_value, median_value, p10_value, p90_value)
        except Exception as e:
            print(f"⚠️  Error creating comprehensive charts: {e}")
            self.create_text_analysis(final_values, mean_value, median_value, p10_value, p90_value)
    
    def create_text_analysis(self, final_values, mean_value, median_value, p10_value, p90_value):
        """Fallback text-based analysis when matplotlib is unavailable"""
        print(f"\n📊 DETAILED ANALYSIS:")
        print("="*50)
        # Additional percentiles    
        p5_value = np.percentile(final_values, 5)
        p95_value = np.percentile(final_values, 95)
        
        print(f"Portfolio Value Distribution:")
        print(f"  5th Percentile:  ${p5_value:,.2f}")
        print(f"  10th Percentile: ${p10_value:,.2f}")
        print(f"  25th Percentile: ${np.percentile(final_values, 25):,.2f}")
        print(f"  Median (50th):   ${median_value:,.2f}")
        print(f"  75th Percentile: ${np.percentile(final_values, 75):,.2f}")
        print(f"  90th Percentile: ${p90_value:,.2f}")
        print(f"  95th Percentile: ${p95_value:,.2f}")
        
        # Risk analysis    
        prob_loss = np.mean([val < self.investment_amount for val in final_values]) * 100
        prob_double = np.mean([val >= 2 * self.investment_amount for val in final_values]) * 100
        
        print(f"\nRisk Analysis:")
        print(f"  Probability of Loss: {prob_loss:.1f}%")
        print(f"  Probability of Doubling: {prob_double:.1f}%")
        print(f"  Standard Deviation: ${np.std(final_values):,.2f}")

# Initialize and run the calculator
if __name__ == "__main__":
    try:
        # Initialize calculator
        calculator = CapitalMarketsCalculator()
        
        # Load data and start setup
        calculator.load_capital_markets_data()
        calculator.setup_calculator()
        
    except Exception as e:
        print(f"\n❌ Error running calculator: {e}")
        import traceback
        traceback.print_exc()
    except KeyboardInterrupt:
        print("\n\n❌ Calculator execution cancelled by user.")
