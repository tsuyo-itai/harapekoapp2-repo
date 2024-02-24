import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import "../../assets/stylesheets/Base.scss"
import "../../assets/stylesheets/Header.scss"
import Header from '../../components/Header';

interface Plan {
    id: number;
    name: string;
    price: number;
    rank: number;
}

// プランカードのコンポーネント
const PlanCard: React.FC<{ plan: Plan }> = ({ plan }) => {

  return (
    <>
      <div className="card-plan-list">
        <div className="card-content-plan-list">
          <h3>{plan.name}</h3>
          <p>Price: {plan.price}円</p>
          <p>Rank: {plan.rank}</p>
          {/* 他のプランの情報も表示する場合はここに追加 */}
        </div>
      </div>
    </>
  );
};

// プランリストのコンポーネント
const PlanList: React.FC<{ plans: Plan[] }> = ({ plans }) => {
    const [selectedPlan, setSelectedPlan] = useState<Plan | null>(null);
    const [IsEditPlan, setIsEditPlan] = useState<Plan | null>(null);

    const [Editplan, setEditplan] = useState<Plan>({
        id: 0,
        name: '',
        price: 0,
        rank: 0
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setEditplan((prevData) => ({
          ...prevData,
          [name]: value,
        }));
    };

    // プランを選択したアクション
    const handlePlanClick = (plan: Plan) => {
      setSelectedPlan(plan);
      setIsEditPlan(null);
    };

    const handleUpdatePlanButton = (plan: Plan) => {
        setIsEditPlan(plan);
        setEditplan(plan);
    };

    const UpdatePlan = async (e: React.FormEvent) => {
      e.preventDefault();

      console.log(Editplan);

      try {
          // PUTリクエストを送信
          const response = await axios.put(`http://localhost:8000/api/v1/plan/${Editplan.id}`, Editplan);
    
          // リクエストが成功した場合の処理
          console.log('PUT request successful:', response.data);
          window.alert("Planの更新が完了しました");
        } catch (error) {
          // エラーハンドリング
          console.error('PUT request failed:', error);
        }
        setSelectedPlan(null);
        setIsEditPlan(null);
        // 苦肉の策なので見直しは行うこと
        window.location.reload();
  };
  
    return (
      <div className="plan-list">
        {plans.map((plan) => (
          <div key={plan.id} onClick={() => handlePlanClick(plan)}>
            <PlanCard plan={plan} />
          </div>
        ))}
  
        {/* モーダル */}
        {selectedPlan && (
          <div className="plan-modal">
            <div className="plan-modal-content">
              {IsEditPlan ? (
                  <>
                  <h4>プラン名称</h4>
                  <input
                    type="text"
                    name="name"
                    value={Editplan.name}
                    onChange={handleChange}
                    className="form-text-box"
                  />
                  <h4>価格</h4>
                    <input
                      type="number"
                      name="price"
                      value={Editplan.price}
                      onChange={handleChange}
                      className="form-text-box"
                    />
                  <h4>ランク</h4>
                    <input
                      type="number"
                      name="rank"
                      value={Editplan.rank}
                      onChange={handleChange}
                      className="form-text-box"
                    />
                  <div className='flex-container'>
                    <button onClick={UpdatePlan}>更新</button>
                    <button onClick={() => setSelectedPlan(null)}>閉じる</button>
                  </div>
                  </>
                ):
                (
                  <>
                    <h2>{selectedPlan.name}</h2>
                    <p>Price: ${selectedPlan.price}</p>
                    <p>Rank: {selectedPlan.rank}</p>
                    <div className='flex-container'>
                        <button onClick={() => handleUpdatePlanButton(selectedPlan)}>編集</button>
                        <button onClick={() => setSelectedPlan(null)}>閉じる</button>
                    </div>
                  </>
                )}

            </div>
          </div>
        )}
      </div>
    );
  };

// ビュー
const PlanEditView = () => {
    const [IsAddPlan, setIsAddPlan] = useState(false);
    const [plans, setPlans] = useState<Plan[]>([]);
    const [Inputplan, setInputplan] = useState<Plan>({
      id: 0,
      name: '',
      price: 0,
      rank: 0
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setInputplan((prevData) => ({
          ...prevData,
          [name]: value,
        }));
    };

    // プラン追加を行ったときのアクション
    const handleAddPlanButton = () => {
        setIsAddPlan(!IsAddPlan);
    };

    // プラン一覧の取得
    const fetchPlanData = async () => {
        try {
          // GET リクエストを行う
          const response = await axios.get('http://localhost:8000/api/v1/plans');
          console.log(response);
          // 取得したデータを state に保存
          setPlans(response.data as Plan[]);
          console.log(plans);

        } catch (error) {
          console.error('GET request failed', error);
        }
      };

    // プランの作成
    const CreatePlan = async (e: React.FormEvent) => {
        e.preventDefault();
        console.log(Inputplan);

        try {
            // PUTリクエストを送信
            const response = await axios.post('http://localhost:8000/api/v1/plans', Inputplan);
      
            // リクエストが成功した場合の処理
            console.log('POST request successful:', response.data);
            window.alert("Planの作成が完了しました");
          } catch (error) {
            // エラーハンドリング
            console.error('POST request failed:', error);
          }
        setIsAddPlan(!IsAddPlan);
        fetchPlanData();
    };


    useEffect(() => {
        fetchPlanData();
    }, []); // 空の依存リストを指定することで、コンポーネントがマウントされたときのみ実行

    return (
        <>
          <Header />
          <h2>Available Plans</h2>
          <button onClick={handleAddPlanButton}>プランの追加</button>
          <PlanList plans={plans} />

          {/* モーダル */}
          {IsAddPlan && (
            <div className="plan-modal">
              <div className="plan-modal-content">
                <h2>新規プラン追加</h2>
                <h4>プラン名称</h4>
                <input
                  type="text"
                  name="name"
                  value={Inputplan.name}
                  onChange={handleChange}
                  className="form-text-box"
                />
                <h4>価格</h4>
                <input
                  type="number"
                  name="price"
                  value={Inputplan.price}
                  onChange={handleChange}
                  className="form-text-box"
                />
                <h4>ランク</h4>
                <input
                  type="number"
                  name="rank"
                  value={Inputplan.rank}
                  onChange={handleChange}
                  className="form-text-box"
                />
  
                {/* 他のプランの情報も表示する場合はここに追加 */}
                <div className='flex-container'>
                  <input type="submit" value="登録" onClick={CreatePlan} className="submit-button" />
                  <input  type="button" value="キャンセル" onClick={handleAddPlanButton} className="submit-button-cancel" />
                </div>
              </div>
            </div>
          )}
        </>
    );
};

export default PlanEditView;
