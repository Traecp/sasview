def enum(*sequential, **named):
    enums = dict(list(zip(sequential, list(range(len(sequential))))), **named)
    return type('Enum', (), enums)

WIDGETS = enum( 'W_FILENAME',
                'W_QMIN',
                'W_QMAX',
                'W_BACKGROUND',
                'W_SCALE',
                'W_CONTRAST',
                'W_POROD_CST',
                'W_EX_QMIN',
                'W_EX_QMAX',
                'W_ENABLE_LOWQ',
                'W_ENABLE_HIGHQ',
                'W_NPTS_LOWQ',
                'W_NPTS_HIGHQ',
                'W_LOWQ_GUINIER',
                'W_LOWQ_POWER',
                'W_LOWQ_FIT',
                'W_LOWQ_FIX',
                'W_LOWQ_POWER_VALUE',
                'W_HIGHQ_FIT',
                'W_HIGHQ_FIX',
                'W_HIGHQ_POWER_VALUE',
                # results
                'W_VOLUME_FRACTION',
                'W_VOLUME_FRACTION_ERR',
                'W_SPECIFIC_SURFACE',
                'W_SPECIFIC_SURFACE_ERR',
                'W_INVARIANT',
                'W_INVARIANT_ERR',
                # for the details widget
                'D_TOTAL_QSTAR',
                'D_TOTAL_QSTAR_ERR',
                'D_LOW_QSTAR',
                'D_LOW_QSTAR_ERR',
                'D_HIGH_QSTAR',
                'D_HIGH_QSTAR_ERR',
)
