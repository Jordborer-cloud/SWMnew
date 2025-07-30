#!/usr/bin/env python3d data if Excel loading fails
"""f.asset_data_nominal = {
Capital Markets Calculator - Interactive Future Projectionsy': 0.1650},
A comprehensive wealth management tool for forward-looking portfolio analysis using capital markets expectations.
This calculator provides Monte Carlo simulations and risk analysis for various asset classes.
""" 'Global Private Debt': {'Expected Return': 0.0800, 'Volatility': 0.1000},
    'Global Diversified Alternatives': {'Expected Return': 0.1100, 'Volatility': 0.1200},
import pandas as pdExpected Return': 0.1300, 'Volatility': 0.3000},
import numpy as npturn USD': {'Expected Return': 0.0625, 'Volatility': 0.0200},
from datetime import datetimeD': {'Expected Return': 0.0700, 'Volatility': 0.0200},
import warningsapital Protected USD': {'Expected Return': 0.0800, 'Volatility': 0.0250},
warnings.filterwarnings('ignore')': 0.0450, 'Volatility': 0.0200}
}
# Note: matplotlib will be imported only when needed for visualizations
# Calculate real returns by subtracting inflation rate
class CapitalMarketsCalculator:
    """Interactive Capital Markets Calculator for future portfolio projections"""
    'Global Bonds': {'Expected Return': 0.0100, 'Volatility': 0.0600},
    def __init__(self):l Estate': {'Expected Return': 0.0900, 'Volatility': 0.1400},
        self.investment_amount = 0ted Return': 0.0500, 'Volatility': 0.1000},
        self.allocation = {}rnatives': {'Expected Return': 0.0800, 'Volatility': 0.1200},
        self.currency = "USD"eturn': 0.1000, 'Volatility': 0.3000},
        self.time_horizon = 10  # years Return': 0.0325, 'Volatility': 0.0200},
        self.num_simulations = 10000xpected Return': 0.0400, 'Volatility': 0.0200},
        self.return_type = "real"  # "real" or "nominal": 0.0500, 'Volatility': 0.0250},
        self.inflation_rate = 0.030  # 3.0% annual inflation assumption
        bin/env python3
        # Load SWAN Capital Markets Data from Excel
        self.load_capital_markets_data() Future Projections
        hensive wealth management tool for forward-looking portfolio analysis using capital markets expectations.
        self.available_assets = list(self.asset_data_real.keys())s for various asset classes.
        
        # Start interactive setup
        self.setup_calculator()
    rt numpy as np
    def load_capital_markets_data(self):
        """Load SWAN Capital Markets data from Excel file"""
        try:terwarnings('ignore')
            print("Loading SWAN Capital Markets data from Excel...")
            lotlib will be imported only when needed for visualizations
            # Load data from Excel
            excel_path = "/Users/jordinborer/Library/CloudStorage/OneDrive-Personal/Wealth Management Clients/Dev/SWM/SWM Updated/SWAN Capital Market Ass.xlsx"
            df = pd.read_excel(excel_path, sheet_name='Capital Market')ections"""
            
            # Initialize data dictionaries
            self.asset_data_nominal = {}
            self.asset_data_real = {}
            .currency = "USD"
            # Process each asset# years
            for _, row in df.iterrows():
                asset_name = row['Asset Class']"nominal"
                nominal_return = row['Nominal Return']lation assumption
                real_return = row['Real Return']
                volatility = row['Volatlity']  # Note: typo in Excel column name
                d_capital_markets_data()
                # Store nominal returns data
                self.asset_data_nominal[asset_name] = {al.keys())
                    'Expected Return': nominal_return,
                    'Volatility': volatility
                }p_calculator()
                
                # Store real returns data
                self.asset_data_real[asset_name] = { file"""
                    'Expected Return': real_return,
                    'Volatility': volatilityets data from Excel...")
                }
            # Load data from Excel
            print("✅ SWAN Capital Markets data loaded successfully!")Drive-Personal/Wealth Management Clients/Dev/SWM/SWM Updated/SWAN Capital Market Ass.xlsx"
            print(f"📊 Available asset classes: {list(self.asset_data_real.keys())}")
            
        except Exception as e:dictionaries
            print(f"❌ Error loading capital markets data: {e}")
            print("Using fallback hardcoded data...")
            
            # Fallback to hardcoded data if Excel loading fails
            self.asset_data_nominal = {:
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
               # Store real returns data
            # Calculate real returns by subtracting inflation rate    self.asset_data_real[asset_name] = {
            self.asset_data_real = {': real_return,
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
    elf.asset_data_nominal = {
    def setup_calculator(self):            'Global Equity': {'Expected Return': 0.0800, 'Volatility': 0.165},
        """Interactive setup for the calculator"""y': {'Expected Return': 0.0400, 'Volatility': 0.100},
        print("="*60): 0.0450, 'Volatility': 0.005},
        print("📊 CAPITAL MARKETS CALCULATOR - FUTURE PROJECTIONS")al Private Real Estate': {'Expected Return': 0.1200, 'Volatility': 0.100},
        print("="*60)'Volatility': 0.080},
        print("Welcome to the interactive Capital Markets Calculator!")al Diversified Alternatives': {'Expected Return': 0.1100, 'Volatility': 0.120},
        print("This tool provides forward-looking projections using capital markets expectations.")0.250},
        print("\n🔮 Based on SWAN Capital Markets Data (from Excel)")
        print(f"📅 Analysis Period: {self.time_horizon} years")00, 'Volatility': 0.020},
        print(f"🎲 Monte Carlo Simulations: {self.num_simulations:,}")turn': 0.0800, 'Volatility': 0.025},
        print(f"📊 Return Types: Nominal vs Real (from Excel columns)")0.005}
        print(f"💹 Inflation Rate: 3.0% (from Excel data)")
        
        # Get investment amount    self.asset_data_real = {
        self.get_investment_amount(): {'Expected Return': 0.0500, 'Volatility': 0.165},
        'Expected Return': 0.0100, 'Volatility': 0.100},
        # Get return type preference        'Global Bonds': {'Expected Return': 0.0150, 'Volatility': 0.005},
        self.get_return_type() Estate': {'Expected Return': 0.0900, 'Volatility': 0.100},
        e Debt': {'Expected Return': 0.0600, 'Volatility': 0.080},
        # Get allocation        'Global Diversified Alternatives': {'Expected Return': 0.0800, 'Volatility': 0.120},
        self.show_preset_allocations()VC': {'Expected Return': 0.1000, 'Volatility': 0.250},
        ': {'Expected Return': 0.0325, 'Volatility': 0.020},
        # Validate and proceed        'Guaranteed Investment USD': {'Expected Return': 0.0400, 'Volatility': 0.020},
        if self.validate_allocation():tal Protected USD': {'Expected Return': 0.0500, 'Volatility': 0.025},
            self.run_calculator() Return': 0.0150, 'Volatility': 0.005}
        else:
            print("❌ Setup incomplete. Please restart the calculator.")
    
    def get_investment_amount(self):    """Interactive setup for the calculator"""
        """Get investment amount from user"""
        print(f"\n💰 INVESTMENT AMOUNT:")- FUTURE PROJECTIONS")
        print("="*40)
        e to the interactive Capital Markets Calculator!")
        while True:print("This tool provides forward-looking projections using capital markets expectations.")
            try: Based on SWAN Capital Markets Data (from Excel)")
                amount_input = input("Enter your investment amount (USD): $")📅 Analysis Period: {self.time_horizon} years")
                # Remove any formatting characters
                amount_str = amount_input.replace(',', '').replace('$', '').strip()from Excel columns)")
                amount = float(amount_str)
                
                if amount <= 0:vestment amount
                    print("⚠️  Please enter a positive amount.")unt()
                    continue
                    eference
                self.investment_amount = amounturn_type()
                print(f"✅ Investment amount set: ${self.investment_amount:,.2f} USD")
                break
                set_allocations()
            except ValueError:
                print("⚠️  Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n❌ Setup cancelled.")
                exit()
    etup incomplete. Please restart the calculator.")
    def get_return_type(self):
        """Get return type preference from user"""self):
        print(f"\n📊 RETURN TYPE SELECTION:")
        print("="*40)
        print("Choose the type of returns for your analysis:")
        print("  1. Real Returns (from Excel 'Real Return' column)")
        print("  2. Nominal Returns (from Excel 'Nominal Return' column)")
        print(f"\n💡 Inflation rate from Excel: {self.inflation_rate*100:.1f}% annually")
        
        while True:        # Remove any formatting characters
            choice = input(f"\nSelect return type (1-2): ").strip()unt_str = amount_input.replace(',', '').replace('$', '').strip()
            
            if choice == "1":    
                self.return_type = "real"0:
                print("✅ Real returns selected (from Excel 'Real Return' column)")er a positive amount.")
                break
            elif choice == "2":
                self.return_type = "nominal"_amount = amount
                print("✅ Nominal returns selected (from Excel 'Nominal Return' column)")set: ${self.investment_amount:,.2f} USD")
                break
            else:
                print("⚠️  Please enter 1 or 2.")t ValueError:
    umber.")
    @property        except KeyboardInterrupt:
    def asset_data(self):   print("\n❌ Setup cancelled.")
        """Return the appropriate asset data based on return type"""
        return self.asset_data_real if self.return_type == "real" else self.asset_data_nominal
    
    def show_asset_classes(self):    """Get return type preference from user"""
        """Display available asset classes with their expected returns and volatilities"""SELECTION:")
        print(f"\n📋 AVAILABLE ASSET CLASSES:")
        print("="*70)our analysis:"
        print(f"{'#':<3} {'Asset Class':<35} {'Exp. Return':<12} {'Volatility':<10}")eal Returns (from Excel 'Real Return' column)")
        print("-" * 70)
        flation rate from Excel: {self.inflation_rate*100:.1f}% annually")
        for i, asset in enumerate(self.available_assets):
            ret = self.asset_data[asset]['Expected Return'] * 100
            vol = self.asset_data[asset]['Volatility'] * 100()
            print(f"{i+1:<3} {asset:<35} {ret:>6.1f}%{'':<8} {vol:>5.1f}%")
    
    def get_user_allocation(self):            self.return_type = "real"
        """Get asset allocation from user with support for multiple assets"""rns selected (from Excel 'Real Return' column)")
        print(f"\n🎯 ASSET ALLOCATION:")
        print("="*40)
        print("Enter the asset numbers and allocation percentages for your portfolio.")return_type = "nominal"
        print("Allocation percentages must sum to 100%"))
        print("Enter 0 when finished adding assets.")
        
        self.allocation = {}        print("⚠️  Please enter 1 or 2.")
        total_allocated = 0
        
        while True:asset_data(self):
            try:he appropriate asset data based on return type"""
                # Show current allocationelf.asset_data_real if self.return_type == "real" else self.asset_data_nominal
                if self.allocation:
                    print(f"\nCurrent allocation:")
                    for asset, weight in self.allocation.items():ir expected returns and volatilities"""
                        print(f"  {asset}: {weight*100:.1f}%")
                    print(f"  Total allocated: {total_allocated:.1f}%")
                    print(f"  Remaining: {100-total_allocated:.1f}%")tility':<10}")
                
                # Get asset selection
                asset_input = input(f"\nEnter asset number (1-{len(self.available_assets)}, or 0 to finish): ")f.available_assets):
                asset_num = int(asset_input)
                latility'] * 100
                if asset_num == 0:t(f"{i+1:<3} {asset:<35} {ret:>6.1f}%{'':<8} {vol:>5.1f}%")
                    break
                    on(self):
                if asset_num < 1 or asset_num > len(self.available_assets): allocation from user with support for multiple assets"""
                    print(f"⚠️  Please enter a number between 1-{len(self.available_assets)}")
                    continue
                et numbers and allocation percentages for your portfolio.")
                asset_name = self.available_assets[asset_num - 1]llocation percentages must sum to 100%")
                
                if asset_name in self.allocation:
                    print(f"⚠️  {asset_name} already allocated. Skipping...")
                    continue
                
                # Get allocation percentageue:
                remaining = 100 - total_allocated
                pct_input = input(f"Enter allocation % for {asset_name} (remaining: {remaining:.1f}%): ")
                pct = float(pct_input.replace('%', ''))
                
                if pct <= 0:    for asset, weight in self.allocation.items():
                    print("⚠️  Please enter a positive percentage.")t(f"  {asset}: {weight*100:.1f}%")
                    continue%")
                      Remaining: {100-total_allocated:.1f}%")
                if total_allocated + pct > 100.1:
                    print(f"⚠️  This would exceed 100% allocation. Maximum remaining: {remaining:.1f}%")
                    continuesh): ")
                int(asset_input)
                # Add to allocation
                self.allocation[asset_name] = pct / 100
                total_allocated += pct
                
                print(f"✅ Added {asset_name}: {pct:.1f}%")if asset_num < 1 or asset_num > len(self.available_assets):
                een 1-{len(self.available_assets)}")
                # Check if we've reached 100%    continue
                if abs(total_allocated - 100) < 0.1:
                    print("✅ Allocation complete (100%)")sset_num - 1]
                    break
                name in self.allocation:
            except ValueError:    print(f"⚠️  {asset_name} already allocated. Skipping...")
                print("⚠️  Please enter valid numbers.")
            except KeyboardInterrupt:
                print("\n❌ Input cancelled.")entage
                return Falseated
        input(f"Enter allocation % for {asset_name} (remaining: {remaining:.1f}%): ")
        # Validate final allocation        pct = float(pct_input.replace('%', ''))
        if abs(total_allocated - 100) > 0.1:
            print(f"⚠️  Total allocation is {total_allocated:.1f}% (should be 100%)")
            return False
        inue
        print(f"\n✅ Final allocation:")            
        for asset, weight in self.allocation.items():t > 100.1:
            print(f"   {asset}: {weight*100:.1f}%")% allocation. Maximum remaining: {remaining:.1f}%")
        
        return True        
    dd to allocation
    def show_preset_allocations(self):            self.allocation[asset_name] = pct / 100
        """Show preset allocation options for quick selection"""
        print(f"\n🎯 QUICK ALLOCATION PRESETS:")
        print("="*40)ct:.1f}%")
        
        presets = {        # Check if we've reached 100%
            '1': {'name': 'Conservative Growth', 'Global Equity': 30, 'Global Bonds': 60, 'USD Cash': 10},abs(total_allocated - 100) < 0.1:
            '2': {'name': 'Moderate Growth', 'Global Equity': 50, 'Global Bonds': 40, 'USD Cash': 10},
            '3': {'name': 'Aggressive Growth', 'Global Equity': 70, 'Global Bonds': 25, 'USD Cash': 5},
            '4': {'name': 'Diversified Alternative', 'Global Equity': 40, 'Global Bonds': 30, 'Global Diversified Alternatives': 20, 'USD Cash': 10},
            '5': {'name': 'Private Markets', 'Global Equity': 30, 'Global Private Real Estate': 25, 'Global Private Debt': 25, 'Global Bonds': 15, 'USD Cash': 5},
            '6': {'name': 'Custom', 'description': 'Build your own allocation'}
        }
               print("\n❌ Input cancelled.")
        for key, preset in presets.items():        return False
            if key != '6':
                assets_str = ', '.join([f"{pct}% {asset}" for asset, pct in preset.items() if asset != 'name'])llocation
                print(f"  {key}. {preset['name']}: {assets_str}")
            else:% (should be 100%)")
                print(f"  {key}. {preset['name']}: {preset['description']}")n False
        
        while True:print(f"\n✅ Final allocation:")
            choice = input(f"\nSelect allocation (1-6): ").strip()weight in self.allocation.items():
            
            if choice in presets:
                if choice == '6':
                    # Custom allocation
                    self.show_asset_classes()
                    success = self.get_user_allocation() quick selection"""
                    if success:
                        break
                else:
                    # Use preset
                    preset = presets[choice]rvative Growth', 'Global Equity': 30, 'Global Bonds': 60, 'USD Cash': 10},
                    self.allocation = {} 'Global Equity': 50, 'Global Bonds': 40, 'USD Cash': 10},
                    for asset, pct in preset.items():owth', 'Global Equity': 70, 'Global Bonds': 25, 'USD Cash': 5},
                        if asset != 'name':'Global Equity': 40, 'Global Bonds': 30, 'Global Diversified Alternatives': 20, 'USD Cash': 10},
                            self.allocation[asset] = pct / 100, 'Global Equity': 30, 'Global Private Real Estate': 25, 'Global Private Debt': 25, 'Global Bonds': 15, 'USD Cash': 5},
                     own allocation'}
                    print(f"\n✅ {preset['name']} allocation selected:")
                    for asset, weight in self.allocation.items():
                        print(f"   {asset}: {weight*100:.1f}%")
                    break
            else:r = ', '.join([f"{pct}% {asset}" for asset, pct in preset.items() if asset != 'name'])
                print("⚠️  Please enter a number between 1-6.")rint(f"  {key}. {preset['name']}: {assets_str}")
    
    def validate_allocation(self):            print(f"  {key}. {preset['name']}: {preset['description']}")
        """Validate and display the user's asset allocation"""
        if not self.allocation or not self.investment_amount:
            return Falserip()
            
        total_allocation = sum(self.allocation.values())if choice in presets:
        
        print(f"\n🔧 USER CONFIGURATION:")            # Custom allocation
        print(f"💰 Investment Amount: ${self.investment_amount:,} {self.currency}")s()
        print(f"📈 Analysis Type: FUTURE PROJECTIONS (CAPITAL MARKETS)")
        print(f"🎯 Asset Allocation:")
        
        for asset, weight in self.allocation.items():        else:
            if weight > 0:
                exp_ret = self.asset_data[asset]['Expected Return'] * 100 = presets[choice]
                vol = self.asset_data[asset]['Volatility'] * 100
                print(f"   {asset}: {weight*100:.1f}% (Exp: {exp_ret:.1f}%, Vol: {vol:.1f}%)")
        
        print(f"\n📊 Total Allocation: {total_allocation*100:.1f}%")                    self.allocation[asset] = pct / 100
        
        if abs(total_allocation - 1.0) > 0.001:            print(f"\n✅ {preset['name']} allocation selected:")
            print("❌ Error: Total allocation must equal 100%")llocation.items():
            return False)
        k
        return True    else:
    nt("⚠️  Please enter a number between 1-6.")
    def run_calculator(self):
        """Main function to run the capital markets calculator"""elf):
        try:
            print(f"\n" + "="*60)ot self.allocation or not self.investment_amount:
            print("📊 CAPITAL MARKETS CALCULATOR - FUTURE PROJECTIONS")
            print("="*60)
            print(f"💰 Investment Amount: ${self.investment_amount:,.2f} {self.currency}")= sum(self.allocation.values())
            print(f"📈 Analysis Type: FORWARD-LOOKING PROJECTIONS")
            print(f"📊 Return Type: {'Real (Inflation-Adjusted)' if self.return_type == 'real' else 'Nominal (Including Inflation)'}")
            if self.return_type == "nominal":
                print(f"💹 Inflation Assumption: {self.inflation_rate*100:.1f}% annually")ECTIONS (CAPITAL MARKETS)")
            print("🎯 Your Asset Allocation:")
            for asset, weight in self.allocation.items():
                if weight > 0:
                    print(f"   {asset}: {weight*100:.1f}%")
            Return'] * 100
            # Portfolio statistics    vol = self.asset_data[asset]['Volatility'] * 100
            print(f"\n📊 PORTFOLIO STATISTICS:"): {weight*100:.1f}% (Exp: {exp_ret:.1f}%, Vol: {vol:.1f}%)")
            expected_return = 0
            portfolio_variance = 0cation: {total_allocation*100:.1f}%")
            
            # Calculate weighted expected return and variancebs(total_allocation - 1.0) > 0.001:
            for asset, weight in self.allocation.items():)
                expected_return += weight * self.asset_data[asset]['Expected Return']
                portfolio_variance += (weight ** 2) * (self.asset_data[asset]['Volatility'] ** 2)
            
            portfolio_volatility = np.sqrt(portfolio_variance)
            
            print(f"   📈 Expected Annual Return: {expected_return*100:.2f}% ({'Real' if self.return_type == 'real' else 'Nominal'})")ain function to run the capital markets calculator"""
            print(f"   📉 Portfolio Volatility: {portfolio_volatility*100:.2f}%")
            risk_free_rate = self.asset_data['USD Cash']['Expected Return']  # Using cash rate as risk-free
            sharpe_ratio = (expected_return - risk_free_rate) / portfolio_volatility
            print(f"   📊 Sharpe Ratio: {sharpe_ratio:.2f}")
            
            # Run Monte Carlo Simulationprint("="*60)
            print(f"\n🎲 MONTE CARLO SIMULATION ({self.num_simulations:,} simulations):"): ${self.investment_amount:,.2f} {self.currency}")
            
            final_values = []print(f"📊 Return Type: {'Real (Inflation-Adjusted)' if self.return_type == 'real' else 'Nominal (Including Inflation)'}")
            yearly_values = []  # Store year-by-year progression for additional chartspe == "nominal":
            ly")
            for simulation in range(self.num_simulations):print("🎯 Your Asset Allocation:")
                value = self.investment_amount
                year_path = [value]
                et}: {weight*100:.1f}%")
                for year in range(self.time_horizon):
                    annual_return = np.random.normal(expected_return, portfolio_volatility)
                    value *= (1 + annual_return)
                    year_path.append(value)
                
                final_values.append(value)
                yearly_values.append(year_path)return and variance
            n.items():
            final_values = np.array(final_values)    expected_return += weight * self.asset_data[asset]['Expected Return']
            2) * (self.asset_data[asset]['Volatility'] ** 2)
            # Calculate statistics
            mean_value = np.mean(final_values) np.sqrt(portfolio_variance)
            median_value = np.median(final_values)
            p10_value = np.percentile(final_values, 10){expected_return*100:.2f}% ({'Real' if self.return_type == 'real' else 'Nominal'})")
            p90_value = np.percentile(final_values, 90)lio_volatility*100:.2f}%")
            rn / portfolio_volatility):.2f}")
            print(f"   💰 Expected Value (Mean): ${mean_value:,.2f} {self.currency}")
            print(f"   📊 Median Value: ${median_value:,.2f} {self.currency}")
            print(f"   📉 10th Percentile: ${p10_value:,.2f} {self.currency}")lations):")
            print(f"   📈 90th Percentile: ${p90_value:,.2f} {self.currency}")
            
            # Calculate returnsyearly_values = []  # Store year-by-year progression for additional charts
            mean_return = ((mean_value / self.investment_amount) ** (1/self.time_horizon) - 1) * 100
            total_return = ((mean_value / self.investment_amount) - 1) * 100
            
            print(f"\n📈 PROJECTED RETURNS ({'Real' if self.return_type == 'real' else 'Nominal'}):")    year_path = [value]
            print(f"   💹 Annualized Return: {mean_return:.2f}% per year")
            print(f"   💰 Total Return: {total_return:.2f}% over {self.time_horizon} years")
            print(f"   💵 Total Gain: ${mean_value - self.investment_amount:,.2f} {self.currency}")
            
            # Calculate real purchasing power if using nominal returns        year_path.append(value)
            if self.return_type == "nominal":
                real_final_values = final_values / ((1 + self.inflation_rate) ** self.time_horizon)
                real_mean_value = np.mean(real_final_values)
                real_mean_return = ((real_mean_value / self.investment_amount) ** (1/self.time_horizon) - 1) * 100
                
                print(f"\n💰 REAL PURCHASING POWER (Inflation-Adjusted):")
                print(f"   💰 Real Value (Mean): ${real_mean_value:,.2f} {self.currency}")
                print(f"   💹 Real Annualized Return: {real_mean_return:.2f}% per year")
            
            # Create comprehensive visualizationsp10_value = np.percentile(final_values, 10)
            self.create_comprehensive_charts(final_values, yearly_values, mean_value, median_value, p10_value, p90_value)s, 90)
            
            print(f"\n✅ Capital markets projections analysis complete!")print(f"   💰 Expected Value (Mean): ${mean_value:,.2f} {self.currency}")
                ncy}")
        except Exception as e:t(f"   📉 10th Percentile: ${p10_value:,.2f} {self.currency}")
            print(f"❌ Error in calculation: {e}") Percentile: ${p90_value:,.2f} {self.currency}")
            import traceback
            traceback.print_exc()rns
    value / self.investment_amount) ** (1/self.time_horizon) - 1) * 100
    def create_comprehensive_charts(self, final_values, yearly_values, mean_value, median_value, p10_value, p90_value):        total_return = ((mean_value / self.investment_amount) - 1) * 100
        """Create comprehensive visualization suite for projections"""
        try:e == 'real' else 'Nominal'}):")
            import matplotlib.pyplot as pltprint(f"   💹 Annualized Return: {mean_return:.2f}% per year")
            tal_return:.2f}% over {self.time_horizon} years")
            # Create a figure with multiple subplotsprint(f"   💵 Total Gain: ${mean_value - self.investment_amount:,.2f} {self.currency}")
            fig = plt.figure(figsize=(20, 15))
            if using nominal returns
            # 1. Distribution histogram (top left)if self.return_type == "nominal":
            ax1 = plt.subplot(3, 3, 1) ((1 + self.inflation_rate) ** self.time_horizon)
            ax1.hist(final_values, bins=50, alpha=0.7, color='skyblue', edgecolor='black')ean(real_final_values)
            ax1.axvline(mean_value, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_value:,.0f}')time_horizon) - 1) * 100
            ax1.axvline(median_value, color='orange', linestyle='--', linewidth=2, label=f'Median: ${median_value:,.0f}')
            ax1.axvline(p10_value, color='purple', linestyle='--', linewidth=1, label=f'10th %: ${p10_value:,.0f}')
            ax1.axvline(p90_value, color='green', linestyle='--', linewidth=1, label=f'90th %: ${p90_value:,.0f}')
            ax1.set_xlabel(f'Portfolio Value after {self.time_horizon} years')
            ax1.set_ylabel('Frequency')
            ax1.set_title(f'Distribution of Final Values\n({self.num_simulations:,} Simulations)')alizations
            ax1.legend(fontsize=8), p10_value, p90_value)
            ax1.grid(True, alpha=0.3)
            ts projections analysis complete!")
            # 2. Box plot (top center)    
            ax2 = plt.subplot(3, 3, 2)
            ax2.boxplot(final_values, vert=True)tion: {e}")
            ax2.set_ylabel(f'Portfolio Value after {self.time_horizon} years')
            ax2.set_title('Value Distribution Summary')
            ax2.grid(True, alpha=0.3)
            elf, final_values, yearly_values, mean_value, median_value, p10_value, p90_value:
            # 3. Percentile progression over time (top right)reate comprehensive visualization suite for projections"""
            ax3 = plt.subplot(3, 3, 3)
            yearly_array = np.array(yearly_values)s plt
            years = list(range(self.time_horizon + 1))
            
            # Calculate percentiles for each yearfig = plt.figure(figsize=(20, 15))
            p10_progression = [np.percentile(yearly_array[:, year], 10) for year in range(self.time_horizon + 1)]
            p25_progression = [np.percentile(yearly_array[:, year], 25) for year in range(self.time_horizon + 1)]
            p50_progression = [np.percentile(yearly_array[:, year], 50) for year in range(self.time_horizon + 1)]
            p75_progression = [np.percentile(yearly_array[:, year], 75) for year in range(self.time_horizon + 1)]
            p90_progression = [np.percentile(yearly_array[:, year], 90) for year in range(self.time_horizon + 1)]
            :,.0f}')
            ax3.fill_between(years, p10_progression, p90_progression, alpha=0.2, color='blue', label='10th-90th %')ax3.fill_between(years, p25_progression, p75_progression, alpha=0.4, color='green', label='25th-75th %')
            ax3.plot(years, p50_progression, color='red', linewidth=2, label='Median')
            ax3.set_xlabel('Years')
            ax3.set_ylabel('Portfolio Value')ution of Final Values\n({self.num_simulations:,} Simulations)')
            ax3.set_title('Value Progression Over Time\n(Confidence Bands)')
            ax3.legend(fontsize=8)
            ax3.grid(True, alpha=0.3)
            )
            # 4. Sample paths (middle left)ax2 = plt.subplot(3, 3, 2)
            ax4 = plt.subplot(3, 3, 4)True)
            sample_paths = yearly_values[:100]  # Show first 100 simulations Value after {self.time_horizon} years')
            for path in sample_paths:
                ax4.plot(years, path, alpha=0.1, color='blue')
            ax4.plot(years, p50_progression, color='red', linewidth=3, label='Median Path')
            ax4.set_xlabel('Years')
            ax4.set_ylabel('Portfolio Value') 3)
            ax4.set_title('Sample Simulation Paths\n(100 Random Simulations)')lues)
            ax4.legend(fontsize=8)
            ax4.grid(True, alpha=0.3)
            or each year
            # 5. Return distribution (middle center)p10_progression = [np.percentile(yearly_array[:, year], 10) for year in range(self.time_horizon + 1)]
            ax5 = plt.subplot(3, 3, 5)array[:, year], 25) for year in range(self.time_horizon + 1)]
            annual_returns = [(val/self.investment_amount)**(1/self.time_horizon) - 1 for val in final_values]entile(yearly_array[:, year], 50) for year in range(self.time_horizon + 1)]
            ax5.hist(annual_returns, bins=50, alpha=0.7, color='lightcoral', edgecolor='black')1)]
            mean_annual_return = np.mean(annual_returns)time_horizon + 1)]
            ax5.axvline(mean_annual_return, color='red', linestyle='--', linewidth=2, 
                       label=f'Mean: {mean_annual_return*100:.2f}%')='blue', label='10th-90th %')
            ax5.set_xlabel('Annualized Return'), alpha=0.4, color='green', label='25th-75th %')
            ax5.set_ylabel('Frequency')lor='red', linewidth=2, label='Median')
            ax5.set_title(f'Distribution of Annualized Returns\n({self.return_type.title()} Returns)')
            ax5.legend(fontsize=8)
            ax5.grid(True, alpha=0.3)rogression Over Time\n(Confidence Bands)')
            ax5.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x*100:.1f}%'))
            
            # 6. Probability of positive returns (middle right)
            ax6 = plt.subplot(3, 3, 6)
            positive_returns = [ret > 0 for ret in annual_returns]
            prob_positive = np.mean(positive_returns) * 100imulations
            
            negative_returns = [ret < 0 for ret in annual_returns]    ax4.plot(years, path, alpha=0.1, color='blue')
            prob_negative = np.mean(negative_returns) * 100h=3, label='Median Path')
            
            categories = ['Positive Returns', 'Negative Returns']ax4.set_ylabel('Portfolio Value')
            probabilities = [prob_positive, prob_negative]imulations)')
            colors = ['green', 'red']
            
            bars = ax6.bar(categories, probabilities, color=colors, alpha=0.7)
            ax6.set_ylabel('Probability (%)')
            ax6.set_title(f'Probability of Return Outcomes\n(Over {self.time_horizon} Years)')
            ax6.grid(True, alpha=0.3)in final_values]
            bins=50, alpha=0.7, color='lightcoral', edgecolor='black')
            # Add percentage labels on barsmean_annual_return = np.mean(annual_returns)
            for bar, prob in zip(bars, probabilities): color='red', linestyle='--', linewidth=2, 
                height = bar.get_height()rn*100:.2f}%')
                ax6.text(bar.get_x() + bar.get_width()/2., height + 1,turn')
                        f'{prob:.1f}%', ha='center', va='bottom', fontweight='bold')
            itle()} Returns)')
            # 7. Value at Risk analysis (bottom left)ax5.legend(fontsize=8)
            ax7 = plt.subplot(3, 3, 7)
            var_levels = [1, 5, 10, 25, 50, 75, 90, 95, 99]ter(plt.FuncFormatter(lambda x, p: f'{x*100:.1f}%'))
            var_values = [np.percentile(final_values, level) for level in var_levels]
            
            ax7.plot(var_levels, var_values, 'o-', color='purple', linewidth=2, markersize=6)ax7.axhline(self.investment_amount, color='red', linestyle='--', alpha=0.7, label='Initial Investment')
            ax7.set_xlabel('Percentile')
            ax7.set_ylabel('Portfolio Value')
            ax7.set_title('Value at Risk (VaR) Analysis')et in annual_returns]
            ax7.legend(fontsize=8)00
            ax7.grid(True, alpha=0.3)
            eturns', 'Negative Returns']
            # 8. Growth multiple distribution (bottom center)probabilities = [prob_positive, prob_negative]
            ax8 = plt.subplot(3, 3, 8)
            growth_multiples = [val/self.investment_amount for val in final_values]
            ax8.hist(growth_multiples, bins=50, alpha=0.7, color='gold', edgecolor='black')
            mean_multiple = np.mean(growth_multiples)
            ax8.axvline(mean_multiple, color='red', linestyle='--', linewidth=2, comes\n(Over {self.time_horizon} Years)')
                       label=f'Mean: {mean_multiple:.2f}x')
            ax8.axvline(1.0, color='black', linestyle='-', alpha=0.5, label='Break-even')
            ax8.set_xlabel('Growth Multiple')
            ax8.set_ylabel('Frequency')ilities):
            ax8.set_title(f'Portfolio Growth Multiple\n(Final Value / Initial Investment)')()
            ax8.legend(fontsize=8)
            ax8.grid(True, alpha=0.3)f}%', ha='center', va='bottom', fontweight='bold')
            
            # 9. Asset allocation pie chart (bottom right)# 7. Value at Risk analysis (bottom left)
            ax9 = plt.subplot(3, 3, 9)
            allocation_labels = [], 50, 75, 90, 95, 99]
            allocation_sizes = []ntile(final_values, level) for level in var_levels]
            colors_pie = plt.cm.Set3(np.linspace(0, 1, len(self.allocation)))
            2, markersize=6)
            for asset, weight in self.allocation.items():ax7.axhline(self.investment_amount, color='red', linestyle='--', alpha=0.7, label='Initial Investment')
                if weight > 0:
                    allocation_labels.append(f'{asset}\n{weight*100:.1f}%')rtfolio Value')
                    allocation_sizes.append(weight)
            
            ax9.pie(allocation_sizes, labels=allocation_labels, colors=colors_pie, ax7.grid(True, alpha=0.3)
                   autopct='', startangle=90, textprops={'fontsize': 8})
            ax9.set_title(f'Portfolio Allocation\n({self.return_type.title()} Returns)')
            
            # Format y-axes for financial valuesgrowth_multiples = [val/self.investment_amount for val in final_values]
            for ax in [ax1, ax2, ax3, ax4, ax7]:alpha=0.7, color='gold', edgecolor='black')
                ax.yaxis.set_major_formatter(plt.FuncFormatter(ples)
                    lambda x, p: f'${x/1e6:.1f}M' if x >= 1e6 else f'${x/1e3:.0f}K'))--', linewidth=2, 
            
            plt.suptitle(f'Capital Markets Calculator - Comprehensive Analysis\n'ax8.axvline(1.0, color='black', linestyle='-', alpha=0.5, label='Break-even')
                        f'${self.investment_amount:,.0f} Investment | {self.time_horizon} Years | '
                        f'{self.return_type.title()} Returns', fontsize=16, fontweight='bold')
            
            plt.tight_layout()ax8.legend(fontsize=8)
            plt.subplots_adjust(top=0.93)ha=0.3)
            plt.show()
             allocation pie chart (bottom right)
        except ImportError:ax9 = plt.subplot(3, 3, 9)
            print("📊 Matplotlib not available for comprehensive visualization")ls = []
            # Fallback to simple text-based analysis
            self.create_text_analysis(final_values, mean_value, median_value, p10_value, p90_value)1, len(self.allocation)))
        except Exception as e:
            print(f"⚠️  Error creating comprehensive charts: {e}")in self.allocation.items():
            self.create_text_analysis(final_values, mean_value, median_value, p10_value, p90_value)
    
    def create_text_analysis(self, final_values, mean_value, median_value, p10_value, p90_value):                allocation_sizes.append(weight)
        """Fallback text-based analysis when matplotlib is unavailable"""
        print(f"\n📊 DETAILED ANALYSIS:")lors_pie, 
        print("="*50)=90, textprops={'fontsize': 8})
        itle(f'Portfolio Allocation\n({self.return_type.title()} Returns)')
        # Additional percentiles    
        p5_value = np.percentile(final_values, 5)financial values
        p95_value = np.percentile(final_values, 95)
        ncFormatter(
        print(f"Portfolio Value Distribution:")            lambda x, p: f'${x/1e6:.1f}M' if x >= 1e6 else f'${x/1e3:.0f}K'))
        print(f"  5th Percentile:  ${p5_value:,.2f}")
        print(f"  10th Percentile: ${p10_value:,.2f}") - Comprehensive Analysis\n'
        print(f"  25th Percentile: ${np.percentile(final_values, 25):,.2f}")f} Investment | {self.time_horizon} Years | '
        print(f"  Median (50th):   ${median_value:,.2f}")fontweight='bold')
        print(f"  75th Percentile: ${np.percentile(final_values, 75):,.2f}")
        print(f"  90th Percentile: ${p90_value:,.2f}")
        print(f"  95th Percentile: ${p95_value:,.2f}")
        
        # Risk analysis    
        prob_loss = np.mean([val < self.investment_amount for val in final_values]) * 100
        prob_double = np.mean([val >= 2 * self.investment_amount for val in final_values]) * 100
        
        print(f"\nRisk Analysis:")    self.create_text_analysis(final_values, mean_value, median_value, p10_value, p90_value)
        print(f"  Probability of Loss: {prob_loss:.1f}%")
        print(f"  Probability of Doubling: {prob_double:.1f}%")ts: {e}")
        print(f"  Standard Deviation: ${np.std(final_values):,.2f}") median_value, p10_value, p90_value)

# Initialize and run the calculator    def create_text_analysis(self, final_values, mean_value, median_value, p10_value, p90_value):
if __name__ == "__main__":ysis when matplotlib is unavailable"""
    calculator = CapitalMarketsCalculator()LED ANALYSIS:")
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
    calculator = CapitalMarketsCalculator()
