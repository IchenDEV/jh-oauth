<template>
  <card title="精弘认证 激活" class="auth-panel">
    <div style="margin-bottom:2.5rem;">
      <text-field
        class="margeTop"
        label="精弘通行证"
        type="text"
        v-model="id"
        :valueCheck="idFilter"
        errrText="请输入正确的精弘通行证"
      ></text-field>
      <text-field
        class="margeTop"
        label="证件"
        type="text"
        v-model="idCard"
        :valueCheck="idCardFilter"
        errrText="请输入正确的证件号"
      ></text-field>
      <text-field
        class="margeTop"
        label="邮箱"
        type="text"
        v-model="email"
        :valueCheck="mailFilter"
        errrText="请输入正确的邮箱"
      ></text-field>
      <text-field
        class="margeTop"
        label="密码"
        type="password"
        v-model="password"
        :valueCheck="passFilter"
        errrText="密码强度不够，需要大小写字母和数字"
      ></text-field>
      <text-field
        class="margeTop"
        label="确认密码"
        type="password"
        v-model="passwordAgain"
        :valueCheck="CheckPasswordIsSame"
        errrText="密码不一致"
      ></text-field>
      <div class="margeTopRight">
        <span style="margin:1.5rem;cursor:pointer" @click="tipClick">❓ 提示</span>
        <span style="margin:1.5rem;cursor:pointer" @click="aboutClick">❕ 关于</span>
      </div>
    </div>
    <v-button  text="激活" @click="Activating" :waiting="isWaiting"></v-button>
    <dialog-com :show="isTipClicked" @close="closeDialog">
      <template v-slot:main>{{tipMsg}}</template>
    </dialog-com>
    <dialog-com :show="isError" @close="closeDialog">
      <template v-slot:main>{{errorMsg}}</template>
    </dialog-com>
  </card>
</template>


<script lang="ts">
// 没有接口，未完成
import DialogCom from '../components/Dialog.vue';
import { Component, Prop, Vue, Emit } from 'vue-property-decorator';
import TextField from '../components/TextField.vue';
import VButton from '../components/Button.vue';
import Card from '../components/Card.vue';
import { postData, getData } from '../utils/fetch';
import router from '../router';
import { API, apiMap } from '../utils/api';
import { ActivationRequest, ActivationResponse } from '../interface/backend/user/Activation';
import stringFilter from '../utils/stringFilter';
import { routerPath } from '../utils/routerPath';
import { Error } from '../utils/error';
import BaseView from '../views/BaseView.vue';
@Component({
  components: { TextField, VButton, Card, DialogCom },
})
export default class Activation extends BaseView {
  private id: string = '';
  private password: string = '';
  private passwordAgain: string = '';
  private email: string = '';
  private idCard: string = '';

  private Activating() {
    if (!this.checkInput()) { this.setError(Error.InputError); return; }

    const request: ActivationRequest = {
      id: this.id,
      idCard: this.idCard,
      password: this.password,
      email: this.email,
    };

    this.isWaiting = true;
    postData(API(apiMap.actUser), request)
      .then((res: ActivationResponse) => {
        this.isWaiting = false;
        if (res.shortcut !== 'ok') { throw res.msg; }
        router.push(routerPath.home);
      })
      .catch((e) => { this.setError(e); });
  }

  private checkInput() {
    return this.idFilter(this.id)
      && this.idCardFilter(this.idCard)
      && this.mailFilter(this.email)
      && this.passFilter(this.password)
      && this.password === this.passwordAgain;
  }

  private CheckPasswordIsSame() {
    return this.password === this.passwordAgain;
  }
}
</script>