import matplotlib.pyplot as plt


def graficar(mean, Button, cpk_sql, cp_sql, recuento, dataf, data, toli, tols, fcpl, fcpu, n):
    if mean != 0:
        fig, axes = plt.subplots(1, 2)
        fig.suptitle("grafica " + Button + " CPK " + str(cpk_sql) +
                     " cp " + str(cp_sql) + " n=" + str(recuento))
        axes[0].set_title('cpk')
        axes[0].plot(dataf, label='datos')
        axes[0].plot(data, '--', label='sinfiltrar')
        axes[0].plot([toli] * len(dataf), 'red', label='tol inf')
        axes[0].plot([tols] * len(dataf), 'red', label='tol sup')
        axes[0].plot([fcpl] * len(data), 'green', label='lsl')
        axes[0].plot([fcpu] * len(data), 'green', label='usl')
        axes[0].legend(loc='upper right')
        axes[0].set_ylabel('Nm')
        axes[0].set_xlabel('muestras')
        axes[1].hist(dataf)
        axes[1].set_title('hist')
        axes[1].set_xlim(0, 180)
        axes[1].set_ylabel('muestras')
        axes[1].set_xlabel('Nm')
        # my_path = os.path.abspath(__file__)  # Figures out the absolute path for you in case your working
        # directory moves around.
        my_file = 'graph+' + str(n) + '.png'
        # plt.show()
        fig.savefig('graphs/' + my_file)

    else:
        print('No data' + Button)
