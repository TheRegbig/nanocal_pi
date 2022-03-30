from settings_parser import SettingsParser
from calibration import Calibration
from fastheat import FastHeat

# provide with-as for Settings classes
# make abstract classes "Params", "AnalogParams" and "Device"?
# think about name "self.samples_per_channel"
# think about possible changing of "self._params.input_mode"
# make singletons?
# provide output_folder
# provide commentaries for each class

def main():
    settings = SettingsParser('./settings.json')
    calibration = Calibration().read('./calibration.json')
    time_temp_table = {'time': [0,50,450,550,950,1000],
                        'temp': [0,0,100,100,0,0]}


    with FastHeat(time_temp_table, calibration, settings) as fh:
        voltage_profiles = fh.arm()

    # for debug, remove later
        import matplotlib.pyplot as plt
        fig, ax1 = plt.subplots()
        ax1.plot(voltage_profiles['ch0'])
        ax1.plot(voltage_profiles['ch1'])
        plt.show()


        fh.run(voltage_profiles)
        fh_data = fh.get_ai_data()

        
    # for debug, remove later
        import matplotlib.pyplot as plt
        fig, ax1 = plt.subplots()
        for i in [0,1,2,3]:
            ax1.plot(fh_data[i], label='channel #'+str(i))
        ax1.legend()
        plt.show()

if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print(e)
