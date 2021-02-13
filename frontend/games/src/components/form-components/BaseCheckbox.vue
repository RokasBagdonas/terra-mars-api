<template>
  <div class="field">
    <div class="level">
      <div class="level-item">
        <label class="label" v-if="label">{{ label }}</label>
      </div>
      <div class="level-item">
        <div class="control">
          <input
            class="checkbox"
            type="checkbox"
            :checked="modelValue"
            v-bind="$attrs"
            @change="$emit('update:modelValue', $event.target.checked)"
          />
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    label: {
      type: String,
      default: "",
    },
    modelValue: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
