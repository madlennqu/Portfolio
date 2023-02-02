{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Decision Tree\n",
    "> - Load **arff** data named **churn.arff** & transform it into **pd.DataFrame**.  \n",
    "> - Preprocess the data: Drop some of the variables.  \n",
    "> - Split it into $x$ and $y$.  \n",
    "> - Apply ```sklearn.tree``` to $y$.  \n",
    "> - Install ```IPython``` and ```pydot``` via **Anaconda prompt** for plotting.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/henrytang/PycharmProjects/pythonprog/econ7890/CH8_Machine_Learning-20200910'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import os\n",
    "#os.chdir('/Volumes/GoogleDrive/My Drive/Teaching/PG_Python/Data')\n",
    "#print(os.getcwd())\n",
    "\n",
    "from scipy.io import arff\n",
    "data = arff.loadarff('churn.arff')\n",
    "\n",
    "import pandas as pd\n",
    "df = pd.DataFrame(data[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Windows \n",
    "```python\n",
    "import os  \n",
    "os.chdir('G:\\My Drive\\Teaching\\PG_Python\\Data')\n",
    "print(os.getcwd())\n",
    "\n",
    "from scipy.io import arff\n",
    "data = arff.loadarff('churn.arff')\n",
    "\n",
    "import pandas as pd\n",
    "df = pd.DataFrame(data[0])\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>COLLEGE</th>\n",
       "      <th>INCOME</th>\n",
       "      <th>OVERAGE</th>\n",
       "      <th>LEFTOVER</th>\n",
       "      <th>HOUSE</th>\n",
       "      <th>HANDSET_PRICE</th>\n",
       "      <th>OVER_15MINS_CALLS_PER_MONTH</th>\n",
       "      <th>AVERAGE_CALL_DURATION</th>\n",
       "      <th>REPORTED_SATISFACTION</th>\n",
       "      <th>REPORTED_USAGE_LEVEL</th>\n",
       "      <th>CONSIDERING_CHANGE_OF_PLAN</th>\n",
       "      <th>LEAVE</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b'zero'</td>\n",
       "      <td>31953.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>313378.0</td>\n",
       "      <td>161.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>b'unsat'</td>\n",
       "      <td>b'little'</td>\n",
       "      <td>b'no'</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b'one'</td>\n",
       "      <td>36147.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>800586.0</td>\n",
       "      <td>244.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>b'unsat'</td>\n",
       "      <td>b'little'</td>\n",
       "      <td>b'considering'</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>b'one'</td>\n",
       "      <td>27273.0</td>\n",
       "      <td>230.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>305049.0</td>\n",
       "      <td>201.0</td>\n",
       "      <td>16.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>b'unsat'</td>\n",
       "      <td>b'very_little'</td>\n",
       "      <td>b'perhaps'</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>b'zero'</td>\n",
       "      <td>120070.0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>788235.0</td>\n",
       "      <td>780.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>b'unsat'</td>\n",
       "      <td>b'very_high'</td>\n",
       "      <td>b'considering'</td>\n",
       "      <td>b'LEAVE'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>b'one'</td>\n",
       "      <td>29215.0</td>\n",
       "      <td>208.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>224784.0</td>\n",
       "      <td>241.0</td>\n",
       "      <td>21.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>b'very_unsat'</td>\n",
       "      <td>b'little'</td>\n",
       "      <td>b'never_thought'</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   COLLEGE    INCOME  OVERAGE  LEFTOVER     HOUSE  HANDSET_PRICE  \\\n",
       "0  b'zero'   31953.0      0.0       6.0  313378.0          161.0   \n",
       "1   b'one'   36147.0      0.0      13.0  800586.0          244.0   \n",
       "2   b'one'   27273.0    230.0       0.0  305049.0          201.0   \n",
       "3  b'zero'  120070.0     38.0      33.0  788235.0          780.0   \n",
       "4   b'one'   29215.0    208.0      85.0  224784.0          241.0   \n",
       "\n",
       "   OVER_15MINS_CALLS_PER_MONTH  AVERAGE_CALL_DURATION REPORTED_SATISFACTION  \\\n",
       "0                          0.0                    4.0              b'unsat'   \n",
       "1                          0.0                    6.0              b'unsat'   \n",
       "2                         16.0                   15.0              b'unsat'   \n",
       "3                          3.0                    2.0              b'unsat'   \n",
       "4                         21.0                    1.0         b'very_unsat'   \n",
       "\n",
       "  REPORTED_USAGE_LEVEL CONSIDERING_CHANGE_OF_PLAN     LEAVE  \n",
       "0            b'little'                      b'no'   b'STAY'  \n",
       "1            b'little'             b'considering'   b'STAY'  \n",
       "2       b'very_little'                 b'perhaps'   b'STAY'  \n",
       "3         b'very_high'             b'considering'  b'LEAVE'  \n",
       "4            b'little'           b'never_thought'   b'STAY'  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['COLLEGE', 'INCOME', 'OVERAGE', 'LEFTOVER', 'HOUSE', 'HANDSET_PRICE',\n",
       "       'OVER_15MINS_CALLS_PER_MONTH', 'AVERAGE_CALL_DURATION',\n",
       "       'REPORTED_SATISFACTION', 'REPORTED_USAGE_LEVEL',\n",
       "       'CONSIDERING_CHANGE_OF_PLAN', 'LEAVE'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "d1 = df.drop(['OVER_15MINS_CALLS_PER_MONTH','REPORTED_SATISFACTION','REPORTED_USAGE_LEVEL',\n",
    "              'CONSIDERING_CHANGE_OF_PLAN'], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>COLLEGE</th>\n",
       "      <th>INCOME</th>\n",
       "      <th>OVERAGE</th>\n",
       "      <th>LEFTOVER</th>\n",
       "      <th>HOUSE</th>\n",
       "      <th>HANDSET_PRICE</th>\n",
       "      <th>AVERAGE_CALL_DURATION</th>\n",
       "      <th>LEAVE</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b'zero'</td>\n",
       "      <td>31953.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>313378.0</td>\n",
       "      <td>161.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b'one'</td>\n",
       "      <td>36147.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>800586.0</td>\n",
       "      <td>244.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>b'one'</td>\n",
       "      <td>27273.0</td>\n",
       "      <td>230.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>305049.0</td>\n",
       "      <td>201.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>b'zero'</td>\n",
       "      <td>120070.0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>788235.0</td>\n",
       "      <td>780.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>b'LEAVE'</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>b'one'</td>\n",
       "      <td>29215.0</td>\n",
       "      <td>208.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>224784.0</td>\n",
       "      <td>241.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>b'STAY'</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   COLLEGE    INCOME  OVERAGE  LEFTOVER     HOUSE  HANDSET_PRICE  \\\n",
       "0  b'zero'   31953.0      0.0       6.0  313378.0          161.0   \n",
       "1   b'one'   36147.0      0.0      13.0  800586.0          244.0   \n",
       "2   b'one'   27273.0    230.0       0.0  305049.0          201.0   \n",
       "3  b'zero'  120070.0     38.0      33.0  788235.0          780.0   \n",
       "4   b'one'   29215.0    208.0      85.0  224784.0          241.0   \n",
       "\n",
       "   AVERAGE_CALL_DURATION     LEAVE  \n",
       "0                    4.0   b'STAY'  \n",
       "1                    6.0   b'STAY'  \n",
       "2                   15.0   b'STAY'  \n",
       "3                    2.0  b'LEAVE'  \n",
       "4                    1.0   b'STAY'  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>lalala_b'one'</th>\n",
       "      <th>lalala_b'zero'</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   lalala_b'one'  lalala_b'zero'\n",
       "0              0               1\n",
       "1              1               0\n",
       "2              1               0\n",
       "3              0               1\n",
       "4              1               0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dummy1 = pd.get_dummies(d1['COLLEGE'], prefix='lalala')\n",
    "dummy1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>lalala_b'zero'</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   lalala_b'zero'\n",
       "0               1\n",
       "1               0\n",
       "2               0\n",
       "3               1\n",
       "4               0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dummy1 = pd.get_dummies(d1['COLLEGE'], prefix='lalala',drop_first=True)\n",
    "dummy1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>INCOME</th>\n",
       "      <th>OVERAGE</th>\n",
       "      <th>LEFTOVER</th>\n",
       "      <th>HOUSE</th>\n",
       "      <th>HANDSET_PRICE</th>\n",
       "      <th>AVERAGE_CALL_DURATION</th>\n",
       "      <th>COLLEGE_b'zero'</th>\n",
       "      <th>LEAVE_b'STAY'</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>31953.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>313378.0</td>\n",
       "      <td>161.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>36147.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>800586.0</td>\n",
       "      <td>244.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>27273.0</td>\n",
       "      <td>230.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>305049.0</td>\n",
       "      <td>201.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>120070.0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>788235.0</td>\n",
       "      <td>780.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>29215.0</td>\n",
       "      <td>208.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>224784.0</td>\n",
       "      <td>241.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     INCOME  OVERAGE  LEFTOVER     HOUSE  HANDSET_PRICE  \\\n",
       "0   31953.0      0.0       6.0  313378.0          161.0   \n",
       "1   36147.0      0.0      13.0  800586.0          244.0   \n",
       "2   27273.0    230.0       0.0  305049.0          201.0   \n",
       "3  120070.0     38.0      33.0  788235.0          780.0   \n",
       "4   29215.0    208.0      85.0  224784.0          241.0   \n",
       "\n",
       "   AVERAGE_CALL_DURATION  COLLEGE_b'zero'  LEAVE_b'STAY'  \n",
       "0                    4.0                1              1  \n",
       "1                    6.0                0              1  \n",
       "2                   15.0                0              1  \n",
       "3                    2.0                1              0  \n",
       "4                    1.0                0              1  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2 = ['COLLEGE','LEAVE']\n",
    "for i in d2:\n",
    "    dummies = pd.get_dummies(d1[i], prefix=i,drop_first=True)\n",
    "    d1 = pd.concat([d1, dummies], axis=1)\n",
    "    d1.drop(i, axis=1, inplace=True)\n",
    "d1.head()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>INCOME</th>\n",
       "      <th>OVERAGE</th>\n",
       "      <th>LEFTOVER</th>\n",
       "      <th>HOUSE</th>\n",
       "      <th>HANDSET_PRICE</th>\n",
       "      <th>AVERAGE_CALL_DURATION</th>\n",
       "      <th>College</th>\n",
       "      <th>Leave</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>31953.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>313378.0</td>\n",
       "      <td>161.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>36147.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13.0</td>\n",
       "      <td>800586.0</td>\n",
       "      <td>244.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>27273.0</td>\n",
       "      <td>230.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>305049.0</td>\n",
       "      <td>201.0</td>\n",
       "      <td>15.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>120070.0</td>\n",
       "      <td>38.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>788235.0</td>\n",
       "      <td>780.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>29215.0</td>\n",
       "      <td>208.0</td>\n",
       "      <td>85.0</td>\n",
       "      <td>224784.0</td>\n",
       "      <td>241.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     INCOME  OVERAGE  LEFTOVER     HOUSE  HANDSET_PRICE  \\\n",
       "0   31953.0      0.0       6.0  313378.0          161.0   \n",
       "1   36147.0      0.0      13.0  800586.0          244.0   \n",
       "2   27273.0    230.0       0.0  305049.0          201.0   \n",
       "3  120070.0     38.0      33.0  788235.0          780.0   \n",
       "4   29215.0    208.0      85.0  224784.0          241.0   \n",
       "\n",
       "   AVERAGE_CALL_DURATION  College  Leave  \n",
       "0                    4.0        1      1  \n",
       "1                    6.0        0      1  \n",
       "2                   15.0        0      1  \n",
       "3                    2.0        1      0  \n",
       "4                    1.0        0      1  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Rename 2 columns\n",
    "col_ind = [6,7]\n",
    "new_col = ['College','Leave']\n",
    "old_col = d1.columns[col_ind]\n",
    "d1.rename(columns=dict(zip(old_col,new_col)), inplace=True)\n",
    "d1.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Modeling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = d1['Leave']\n",
    "x = d1.drop(['Leave'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "churn = DecisionTreeClassifier(criterion=\"entropy\",\n",
    "                               min_samples_split=2500,\n",
    "                               min_samples_leaf=2000)  # max_depth = 4\n",
    "\n",
    "churn.fit(x,y)\n",
    "churn_pred = churn.predict(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.65      0.83      0.73      9852\n",
      "           1       0.77      0.57      0.65     10148\n",
      "\n",
      "    accuracy                           0.69     20000\n",
      "   macro avg       0.71      0.70      0.69     20000\n",
      "weighted avg       0.71      0.69      0.69     20000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix,classification_report,precision_score\n",
    "print(classification_report(y,churn_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[8130 1722]\n",
      " [4398 5750]]\n",
      "The accuracy rate is 0.74185\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y,churn_pred))\n",
    "accuracy = (7240+7597)/20000\n",
    "out = 'The accuracy rate is {}'.format(accuracy)\n",
    "print(out)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Installation\n",
    "* Install pydotplus in anaconda\n",
    "* Install Graphviz\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import Image  \n",
    "from sklearn.tree import export_graphviz\n",
    "import pydotplus\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dt_graphviz = export_graphviz(churn, out_file = None)\n",
    "\n",
    "pydot_graph = pydotplus.graph_from_dot_data(dt_graphviz)\n",
    "Image(pydot_graph.create_png())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
