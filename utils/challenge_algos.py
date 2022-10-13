fix_size_prize_logic = {
    "is_active": True,
    "name": "Фиксированная награда за выполнение задания",
    "description": "Награда выдается при подтверждении отчета о выполнении от участника организатором челленджа, "
                   "либо в размере, выбранном организатором, либо первым N участникам, признанными выполнившими "
                   "задание (устанавливается параметрами настройки алгоритма)",
    "calculation_type": "auto",
    "reward_time": "ongoing",
    "params": [
                {"id": 1, "name": "Награда за выполнение (одному участнику)", "type": "N", "default": None},
                {"id": 2, "name": "Количество награждаемых", "type": "N", "default": 5}
              ],
    "grace_period": "1h"
}